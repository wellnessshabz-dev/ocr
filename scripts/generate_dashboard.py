#!/usr/bin/env python3
"""OCR V1 — Folder Structure Visualizer

Generates a live HTML cognition map from the file system tree.
Run: python scripts/generate_dashboard.py
"""

from pathlib import Path
import json


PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT = PROJECT_ROOT / "surfaces" / "executive" / "index.html"


def build_tree(base: Path) -> list:
    entries = []
    for child in sorted(base.iterdir()):
        if child.name.startswith(".") or child.name == "__pycache__":
            continue
        if child.name == "node_modules":
            continue
        entry = {"name": child.name}
        if child.is_dir():
            entry["type"] = "directory"
            entry["children"] = build_tree(child)
        else:
            entry["type"] = "file"
        entries.append(entry)
    return entries


def layer_info(name: str) -> dict:
    layers = {
        "cognition": {"label": "Cognition Runtime", "color": "#3b82f6"},
        "ontology": {"label": "Ontology Engine", "color": "#8b5cf6"},
        "shipments": {"label": "Shipment Pipeline", "color": "#f59e0b"},
        "ledger": {"label": "Cognition Ledger", "color": "#10b981"},
        "gbrain": {"label": "Memory Substrate", "color": "#06b6d4"},
        "orchestration": {"label": "Orchestration", "color": "#ec4899"},
        "ingestion": {"label": "Ingestion", "color": "#6366f1"},
        "surfaces": {"label": "Executive Surfaces", "color": "#84cc16"},
        "replay": {"label": "Replay Engine", "color": "#14b8a6"},
        "agents": {"label": "Agent Layer", "color": "#f97316"},
        "observability": {"label": "Observability", "color": "#a855f7"},
        "infra": {"label": "Infrastructure", "color": "#64748b"},
        "docs": {"label": "Documentation", "color": "#78716c"},
    }
    return layers.get(name, {"label": name, "color": "#6b7280"})


def build_layer_panel():
    dirs = [d for d in PROJECT_ROOT.iterdir() if d.is_dir() and not d.name.startswith(".")]
    html = ""
    for d in sorted(dirs):
        info = layer_info(d.name)
        count = sum(1 for _ in d.rglob("*") if _.is_file())
        html += f"""
        <div class="layer-card" style="border-left: 4px solid {info['color']}">
            <div class="layer-name">{info['label']}</div>
            <div class="layer-path">{d.name}/</div>
            <div class="layer-count">{count} files</div>
        </div>"""
    return html


def build_active_shipments():
    return """
    <div class="shipment-item">
        <div class="shipment-id">No active shipments</div>
        <div class="shipment-status" style="color: #6b7280">awaiting first signal</div>
    </div>"""


def build_adr_list():
    adrs_dir = PROJECT_ROOT / "docs" / "adrs"
    html = ""
    if adrs_dir.exists():
        for f in sorted(adrs_dir.glob("*.md")):
            content = f.read_text()
            title_line = [l for l in content.splitlines() if l.startswith("# ")]
            title = title_line[0][2:].strip() if title_line else f.stem
            html += f"""
            <div class="adr-item">
                <a href="file://{f}" class="adr-title">{title}</a>
            </div>"""
    return html


def generate():
    tree = build_tree(PROJECT_ROOT)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OCR — Cognition Map</title>
<style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: 'Inter', -apple-system, sans-serif; background: #0f172a; color: #e2e8f0; display: flex; min-height: 100vh; }}
    .sidebar {{ width: 300px; background: #1e293b; padding: 1.5rem; overflow-y: auto; border-right: 1px solid #334155; }}
    .main {{ flex: 1; padding: 1.5rem; overflow-y: auto; }}
    .right {{ width: 320px; background: #1e293b; padding: 1.5rem; overflow-y: auto; border-left: 1px solid #334155; }}
    h1 {{ font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #f8fafc; }}
    h2 {{ font-size: 0.875rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; color: #64748b; margin: 1.5rem 0 0.75rem; }}
    h3 {{ font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; color: #64748b; margin: 1rem 0 0.5rem; }}
    .badge {{ display: inline-block; padding: 0.125rem 0.5rem; border-radius: 9999px; font-size: 0.75rem; font-weight: 500; }}
    .badge-foundation {{ background: #3b82f6; color: #eff6ff; }}
    .status {{ display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 0.5rem; }}
    .status-ok {{ background: #10b981; }}
    .status-warn {{ background: #f59e0b; }}
    .status-err {{ background: #ef4444; }}
    .tree-node {{ padding: 0.25rem 0; font-size: 0.8125rem; cursor: pointer; }}
    .tree-node:hover {{ color: #93c5fd; }}
    .tree-folder {{ color: #60a5fa; }}
    .tree-file {{ color: #94a3b8; margin-left: 1rem; }}
    .tree-toggle {{ display: inline-block; width: 1rem; cursor: pointer; color: #64748b; user-select: none; }}
    .tree-children {{ margin-left: 1rem; display: none; }}
    .tree-children.open {{ display: block; }}
    .layer-card {{ padding: 0.75rem; margin-bottom: 0.5rem; background: #334155; border-radius: 0.375rem; }}
    .layer-name {{ font-weight: 600; font-size: 0.875rem; }}
    .layer-path {{ font-size: 0.75rem; color: #64748b; font-family: monospace; }}
    .layer-count {{ font-size: 0.75rem; color: #94a3b8; margin-top: 0.25rem; }}
    .shipment-item, .adr-item {{ padding: 0.5rem; margin-bottom: 0.25rem; background: #334155; border-radius: 0.25rem; font-size: 0.8125rem; }}
    .shipment-id {{ font-family: monospace; color: #60a5fa; }}
    .shipment-status {{ font-size: 0.75rem; margin-top: 0.25rem; }}
    .adr-title {{ color: #a5b4fc; text-decoration: none; }}
    .adr-title:hover {{ color: #c7d2fe; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 0.75rem; }}
    .section {{ background: #1e293b; border-radius: 0.5rem; padding: 1rem; margin-bottom: 1rem; border: 1px solid #334155; }}
</style>
</head>
<body>
<div class="sidebar">
    <h1>🧠 OCR</h1>
    <p style="font-size:0.75rem;color:#64748b;margin-bottom:1.5rem;">Organizational Cognition Runtime</p>

    <div style="margin-bottom:1rem;">
        <span class="status status-ok"></span><span style="font-size:0.8125rem;">All services nominal</span>
    </div>

    <h2>Architecture Layers</h2>
    <div id="layers">
        {build_layer_panel()}
    </div>

    <h2>ADRs</h2>
    <div id="adrs">
        {build_adr_list()}
    </div>
</div>

<div class="main">
    <div class="grid">
        <div class="section">
            <h3>Folder Structure</h3>
            <div id="tree">
                {render_tree(tree)}
            </div>
        </div>
        <div class="section">
            <h3>Cognition Pipeline</h3>
            <div style="font-size:0.8125rem;line-height:2;">
                <div>📥 Signal →</div>
                <div style="margin-left:1rem;">📦 Shipment →</div>
                <div style="margin-left:2rem;">🔍 Ontology Extraction →</div>
                <div style="margin-left:3rem;">🧠 Memory Activation →</div>
                <div style="margin-left:4rem;">⚖️ Council →</div>
                <div style="margin-left:5rem;">✍️ Chairman Synthesis →</div>
                <div style="margin-left:6rem;">💾 Postgres Ledger →</div>
                <div style="margin-left:7rem;">📊 Executive Surface</div>
            </div>
        </div>
    </div>

    <div class="grid">
        <div class="section">
            <h3>Shipment Lineage</h3>
            <div id="shipments">
                {build_active_shipments()}
            </div>
        </div>
        <div class="section">
            <h3>Ontology</h3>
            <p style="font-size:0.8125rem;color:#64748b;">No ontology nodes yet. First shipment will seed the graph.</p>
        </div>
    </div>
</div>

<div class="right">
    <h2>Active Questions</h2>
    <div class="adr-item">Which ADR should be written next?</div>
    <div class="adr-item">What is the first signal to process?</div>
    <div class="adr-item">Which council composition for V1?</div>

    <h2 style="margin-top:2rem;">Unresolved Contradictions</h2>
    <p style="font-size:0.8125rem;color:#64748b;">None yet. Contradictions surface after deliberation.</p>

    <h2 style="margin-top:2rem;">Recent Reasoning Sessions</h2>
    <p style="font-size:0.8125rem;color:#64748b;">No sessions recorded. Shipments will populate this view.</p>
</div>

<script>
document.querySelectorAll('.tree-toggle').forEach(toggle => {{
    toggle.addEventListener('click', () => {{
        const children = toggle.parentElement.nextElementSibling;
        if (children) {{
            children.classList.toggle('open');
            toggle.textContent = children.classList.contains('open') ? '▼' : '▶';
        }}
    }});
}});
</script>
</body>
</html>"""

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(html)
    print(f"Dashboard generated: {OUTPUT}")
    print(f"Open: file://{OUTPUT}")


def render_tree(entries, depth=0) -> str:
    html = ""
    indent = depth * 1
    for entry in entries:
        if entry["type"] == "directory":
            html += f"""
            <div class="tree-node" style="margin-left:{indent}rem">
                <span class="tree-toggle">▶</span>
                <span class="tree-folder">📁 {entry['name']}</span>
            </div>
            <div class="tree-children">"""
            if "children" in entry:
                html += render_tree(entry["children"], depth + 1)
            html += "</div>"
        else:
            html += f"""<div class="tree-node tree-file" style="margin-left:{indent + 1}rem">📄 {entry['name']}</div>"""
    return html


if __name__ == "__main__":
    generate()
