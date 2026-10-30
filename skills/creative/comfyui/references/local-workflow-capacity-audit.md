# Local workflow capacity audit

Use this when a user shares a local ComfyUI URL and asks whether the workflow fits their machine.

## Extract a browser-only draft

A `http://127.0.0.1:8188/#<uuid>` workflow may exist only in frontend state, not as a JSON file. After opening it in the browser, inspect `localStorage` keys beginning with `Comfy.Workflow.Draft.v2:`. Each value is an envelope whose `data` field is another JSON string containing the frontend workflow.

Minimal browser-console summary:

```js
(() => {
  const key = Object.keys(localStorage)
    .find(k => k.startsWith('Comfy.Workflow.Draft.v2:'));
  const graph = JSON.parse(JSON.parse(localStorage.getItem(key)).data);
  return {
    id: graph.id,
    nodeCount: graph.nodes.length,
    nodes: graph.nodes.map(n => ({
      id: n.id,
      type: n.type,
      widgets: n.widgets_values || [],
      inputs: (n.inputs || []).map(x => x.name),
      outputs: (n.outputs || []).map(x => x.name),
    })),
  };
})()
```

The hash may be replaced by a new draft ID after import. Validate the extracted nodes and model filenames rather than assuming the post-load hash must remain identical.

## Audit sequence

1. Extract node types, widget values, dimensions, steps, batch size, and every referenced model filename.
2. Check live machine capacity (`system_profiler`, `/system_stats`) and current free unified/VRAM memory.
3. Locate every referenced model under the exact ComfyUI `models/` folder and measure file sizes. Include auxiliary text encoders, VAEs, and LoRAs; the diffusion checkpoint alone understates the footprint.
4. Compare graph semantics with the model’s official native workflow. A graph can have all files installed yet still be structurally wrong—for example, a video/audio model wired through still-image latent and save nodes.
5. Do not prove fit by submitting an expensive generation. First use static inspection or `--print-prompt`; if the graph is valid, run the smallest representative smoke test.
6. Recommend models already installed before suggesting downloads. Give one safe option per intended medium (image/video), with measured local file sizes.

## Capacity judgment

- File-size totals are not exact peak RAM because ComfyUI may load/offload components sequentially, but the largest simultaneously resident model plus activations, OS usage, and output buffers must fit.
- On Apple Silicon, MPS shares system memory. If one model file nearly equals total unified memory, call it impractical even if mmap/offload might technically crawl through swap.
- Separate “can possibly start” from “practical to use.” Heavy swap, multi-hour previews, or likely OS pressure is not a practical fit.
- Resolution, frame count, batch size, precision, and attention implementation materially change activation memory; report them.

## MiniMax H3 exemplar

MiniMax H3 is an omni-modal video model with native stereo audio. Official ComfyUI workflows use native MiniMax H3 T2V/I2V/R2V nodes, both video and audio VAEs, duration on the 17k+5 frame grid at 24 fps, and video output. A graph using `EmptySD3LatentImage` → generic `KSampler` → audio VAE → `SaveImage` is semantically wrong regardless of hardware.

The open-weight H3 stack can include a roughly 20 GiB diffusion model, 15 GiB Qwen3-VL encoder, 5 GiB video VAE, audio VAE, and turbo LoRA. A 24 GB unified-memory Mac is therefore not a practical local target. Prefer Cloud for H3, or a lighter local image/video pair such as SDXL plus Wan 1.3B when those are already installed.

Treat these sizes and model recommendations as an exemplar, not a permanent catalog. Re-measure local files and check current official docs each audit.