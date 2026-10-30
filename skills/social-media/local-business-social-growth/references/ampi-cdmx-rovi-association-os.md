# AMPI CDMX → ROVI Association Operating System Pattern

Session date: 2026-05-22

Use when adapting ROVI/COPIM-style platform proposals to a real estate association or professional chamber from public web presence.

## Public signals observed on AMPI CDMX

Site: `https://ampicdmx.org/`

Visible assets:
- Institutional site for Asociación Mexicana de Profesionales Inmobiliarios Ciudad de México A.C.
- Public pages: Nosotros, Consejo, Directorio, Capacitación y eventos, Beneficios, Requisitos, Revista, Blog, Contacto, Ingresar.
- `¿Qué es AMPI?` states AMPI CDMX was constituted in 1980 and gathers 400+ important companies in the sector.
- Directory link on The Smart Flat showed 108 verified advisors.
- Properties and login are on external Smart Flat / Smart Manager URLs.
- Event example: “7 errores que están saboteando tus cierres”, 2026-05-28, 18:00, Zoom.
- Event flow used external links for payment (WeChamber) and registration (Zoom).
- Pre-registration/contact forms exist, but contact intent is generic.
- Requirements page asks applicants to email documents: application, experience, photo, address proof, fiscal docs, CURP, INE, CV, logo.
- Contact emails visible: `ifernandez@ampicdmx.mx`, `mestrella@ampicdmx.mx`.

## Interpretation pattern

Do not pitch “another CRM.” Pitch a class-level operating system:

> ROVI connects what the association already has — membership, events, directory, properties, payments, communications, magazine, allies, and reports — into one measurable operating layer.

Avoid saying “replace your portal / replace Smart Manager / replace The Smart Flat.” Safer wedge:
- Integrate gradually.
- Start with affiliation + events + directory metrics.
- Demonstrate value in 30 days.

## Module map from ROVI/COPIM

COPIM concepts translate to AMPI as:
- Members → Asociados / asesores / inmobiliarias.
- Membership payments → Cuotas / renovaciones / eventos pagados.
- Marketplace → Directorio + propiedades + aliados + revista/patrocinadores.
- Association admin → Consejo / operación AMPI.
- Knowledge bot → Agente AMPI for requirements, benefits, events, documents, reports.

Recommended modules:
1. CRM de prospectos y pre-registro.
2. Expediente digital del asociado.
3. Portal privado de asociados.
4. Eventos y capacitación with registration, payments, Zoom/check-in, attendance, certificates.
5. Directorio inteligente with verified profiles, specialties, properties, leads, metrics.
6. Propiedades/inventario integrated or tracked externally.
7. Revista, aliados, patrocinadores pipeline.
8. Control Tower for council: active members, prospects, renewals, event metrics, revenue, directory leads.
9. AI agent with AMPI knowledge base.

## MVP 30-day plan

Week 1: tenant, roles, pipelines, sample advisors.
Week 2: pre-registration, digital file, document checklist, follow-up automation.
Week 3: event landing/registration/payment tracking/reminders/attendance/certificate.
Week 4: basic portal + enriched directory + control tower demo.

## Demo sequence

1. New association prospect → checklist → responsible owner → follow-up → active member.
2. Current event → registrants → payment status → Zoom/reminders → attendance → certificate → report.
3. Verified advisor profile → membership status → properties → requests → visibility metrics.
4. Control Tower → prospects, active members, renewals, events, payments, leads, open tasks.

## Deliverables created in session

- Proposal markdown: `/Users/USERNAME/Documents/GitHub/rovi_copim/leadvibes/docs/propuesta/ampi/AMPI_CDMX_ROVI_COPIM_PROPOSAL.md`
- Pitch deck: `/Users/USERNAME/Documents/GitHub/rovi_copim/leadvibes/docs/propuesta/ampi/ROVI_AMPI_CDMX_Pitch_Deck.pptx`

## Messaging pitfall

Sending direct Telegram to a user ID can fail with `Forbidden: bot can't initiate conversation with a user`. If a business partner is in a shared group, mention them there and attach the file instead, after attempting/confirming available targets with `send_message action=list`.
