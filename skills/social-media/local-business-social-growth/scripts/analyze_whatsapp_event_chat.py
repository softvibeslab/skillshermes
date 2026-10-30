#!/usr/bin/env python3
"""Analyze exported WhatsApp community chats for event/promoter monetization.

Inputs: WhatsApp export ZIP or TXT.
Outputs: event_leads.csv, promoter_outreach_targets.csv, monetization_report.md, first_calendar_post.md, summary.json.
"""
import argparse, csv, datetime as dt, json, os, re, shutil, tempfile, urllib.parse, zipfile
from collections import Counter, defaultdict

EVENT_KW = re.compile(r"party|event|tickets?|cover|entry|entrada|rooftop|pool|beach|club|bachata|salsa|kizomba|class|clase|social|tonight|today|hoy|tomorrow|mañana|vip|reservation|booking|mesa|table|workshop|festival|dance|baile|dj|open bar|no cover|free access|wellness|yoga|meditation|karaoke|catamaran|boat|yacht", re.I)
PRICE_RE = re.compile(r"(?:\$|mxn|pesos?|usd)\s?\d+[\d,]*(?:\s?(?:mxn|pesos?|usd))?|\d+[\d,]*\s?(?:mxn|pesos?|usd)", re.I)
LINK_RE = re.compile(r"https?://\S+")
PHONE_RE = re.compile(r"(?:\+?52\s*)?(?:\(?\d{2,3}\)?[\s\-]*){3,5}\d{2,4}")
MSG_RE = re.compile(r"^\[(\d{1,2}/\d{1,2}/\d{2}),\s+([^\]]+)\]\s+([^:\n]{1,100}):\s?(.*)$")


def normalize(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n").replace("\u200e", "").replace("\u202f", " ").replace("\xa0", " ")


def extract_input(input_path: str, workdir: str) -> str:
    if zipfile.is_zipfile(input_path):
        with zipfile.ZipFile(input_path) as zf:
            zf.extractall(workdir)
        txts = []
        for root, _, files in os.walk(workdir):
            for f in files:
                if f.lower().endswith(".txt"):
                    txts.append(os.path.join(root, f))
        if not txts:
            raise SystemExit("No .txt chat file found in ZIP")
        return max(txts, key=os.path.getsize)
    return input_path


def parse_messages(chat_path: str):
    text = normalize(open(chat_path, encoding="utf-8").read())
    messages, cur = [], None
    for line in text.splitlines():
        m = MSG_RE.match(line)
        if m:
            if cur:
                messages.append(cur)
            d, t, sender, body = m.groups()
            cur = {"date": d, "time": t, "sender": sender.strip(), "text": body.strip()}
        elif cur:
            cur["text"] += "\n" + line
    if cur:
        messages.append(cur)
    for m in messages:
        m["dt"] = dt.datetime.strptime(m["date"], "%d/%m/%y").date()
    return messages


def clean_link(l: str) -> str:
    return l.strip().strip(").,]}")


def domains(links):
    c = Counter()
    for l in links:
        try:
            c[urllib.parse.urlparse(clean_link(l)).netloc.lower().replace("www.", "")] += 1
        except Exception:
            pass
    return c


def write_csv(path, rows, fields):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="WhatsApp export .zip or _chat.txt")
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--recent-days", type=int, default=75)
    args = ap.parse_args()
    os.makedirs(args.outdir, exist_ok=True)
    workdir = tempfile.mkdtemp(prefix="wa_export_")
    try:
        chat_path = extract_input(args.input, workdir)
        msgs = parse_messages(chat_path)
        if not msgs:
            raise SystemExit("No messages parsed")
        max_date, min_date = max(m["dt"] for m in msgs), min(m["dt"] for m in msgs)
        cutoff = max_date - dt.timedelta(days=args.recent_days)
        event_msgs = [m for m in msgs if EVENT_KW.search(m["text"])]
        recent_events = [m for m in event_msgs if m["dt"] >= cutoff]

        event_rows = []
        for m in event_msgs:
            tx = m["text"]
            event_rows.append({
                "date": m["date"], "sender": m["sender"],
                "prices": "; ".join(PRICE_RE.findall(tx)),
                "links": "; ".join(clean_link(l) for l in LINK_RE.findall(tx)),
                "text": tx.replace("\n", " / ")[:2000]
            })
        event_csv = os.path.join(args.outdir, "event_leads.csv")
        write_csv(event_csv, event_rows, ["date", "sender", "prices", "links", "text"])

        by = defaultdict(list)
        for m in recent_events:
            by[m["sender"]].append(m)
        target_rows = []
        for sender, arr in by.items():
            full = "\n".join(a["text"] for a in arr)
            links = [clean_link(l) for l in LINK_RE.findall(full)]
            phones = []
            for l in links:
                if "wa.me/" in l:
                    phones.append(re.sub(r"\D", "", l.split("wa.me/", 1)[1].split("?")[0]))
            for p in PHONE_RE.findall(full):
                digits = re.sub(r"\D", "", p)
                if len(digits) >= 10:
                    phones.append(digits)
            igs = []
            for l in links:
                if "instagram.com/" in l:
                    part = urllib.parse.urlparse(l).path.strip("/").split("/")[0]
                    if part and part not in ["p", "reel", "stories"]:
                        igs.append("@" + part)
            igs += re.findall(r"@[A-Za-z0-9._]{3,30}", full)
            prices = PRICE_RE.findall(full)
            sample = max(arr, key=lambda x: len(x["text"]))["text"].replace("\n", " / ")[:700]
            score = len(arr) * 3 + len(set(links)) * 2 + len(set(phones)) * 5 + len(prices)
            target_rows.append({
                "rank_score": score, "sender": sender, "recent_event_posts": len(arr),
                "latest_post": max(a["dt"] for a in arr).isoformat(),
                "phones_or_wa": "; ".join(sorted(set(phones))[:8]),
                "instagram_or_mentions": "; ".join(sorted(set(igs))[:10]),
                "top_domains": "; ".join(f"{d}({c})" for d, c in domains(links).most_common(5)),
                "prices_seen": "; ".join(p for p, _ in Counter(prices).most_common(5)),
                "sample_event": sample,
            })
        target_rows.sort(key=lambda r: (r["rank_score"], r["recent_event_posts"]), reverse=True)
        target_csv = os.path.join(args.outdir, "promoter_outreach_targets.csv")
        if target_rows:
            write_csv(target_csv, target_rows, list(target_rows[0].keys()))

        top_domains = domains([l for m in event_msgs for l in LINK_RE.findall(m["text"])]).most_common(20)
        top_senders = Counter(m["sender"] for m in msgs).most_common(20)
        top_event_posters = Counter(m["sender"] for m in event_msgs).most_common(20)
        report_path = os.path.join(args.outdir, "monetization_report.md")
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(f"# Community Chat Monetization Report\n\n")
            f.write(f"- Messages parsed: {len(msgs)}\n- Period: {min_date} to {max_date}\n- Unique senders: {len(set(m['sender'] for m in msgs))}\n- Event/promotional messages: {len(event_msgs)}\n- Prices found: {sum(1 for m in event_msgs if PRICE_RE.search(m['text']))}\n- Links found: {sum(len(LINK_RE.findall(m['text'])) for m in event_msgs)}\n\n")
            f.write("## Recommended MVP\n\nLaunch a curated channel/newsletter/calendar for the dominant repeated demand in the chat. Start with manual curation and supplier outreach before building an app.\n\n")
            f.write("## Monetization\n- Featured listings/posts\n- Commission per booking/ticket/reservation\n- Weekly supplier/venue package\n- Concierge/recommendation fee\n\n")
            f.write("## Top targets\n")
            for i, r in enumerate(target_rows[:15], 1):
                f.write(f"{i}. {r['sender']} — {r['recent_event_posts']} recent posts; latest {r['latest_post']}\n")
            f.write("\n## Outreach message\n\nHola! Estoy lanzando un calendario bilingüe curado de eventos en la zona. Vi que publicas eventos seguido y quiero incluirte. Esta semana estoy ofreciendo 1 destacado gratis para medir respuesta. Si te mando gente, podemos trabajar con destacado por evento o comisión por reserva/ticket. ¿Quieres que publique tu próximo evento con link/WhatsApp de reserva?\n")

        post_path = os.path.join(args.outdir, "first_calendar_post.md")
        with open(post_path, "w", encoding="utf-8") as f:
            f.write("🔥 *Qué hacer esta semana*\n\nSelección rápida curada desde la comunidad:\n\n")
            for i, r in enumerate(target_rows[:7], 1):
                f.write(f"{i}. *{r['sender']}*\n   - Señal: {r['recent_event_posts']} publicaciones recientes\n")
                if r["prices_seen"]: f.write(f"   - Precios vistos: {r['prices_seen']}\n")
                if r["top_domains"]: f.write(f"   - Links: {r['top_domains']}\n")
                f.write("\n")
            f.write("¿Quieres recibir el calendario diario? Responde *INFO*.\nPromotores: manda tu evento para salir destacado.\n")

        summary = {
            "messages": len(msgs), "period": [min_date.isoformat(), max_date.isoformat()],
            "unique_senders": len(set(m['sender'] for m in msgs)),
            "event_messages": len(event_msgs), "recent_event_messages": len(recent_events),
            "top_senders": top_senders, "top_event_posters": top_event_posters,
            "top_domains": top_domains,
            "files": {"event_leads": event_csv, "targets": target_csv, "report": report_path, "post": post_path},
        }
        summary_path = os.path.join(args.outdir, "summary.json")
        open(summary_path, "w", encoding="utf-8").write(json.dumps(summary, ensure_ascii=False, indent=2, default=str))
        print(json.dumps(summary, ensure_ascii=False, indent=2, default=str))
    finally:
        shutil.rmtree(workdir, ignore_errors=True)

if __name__ == "__main__":
    main()
