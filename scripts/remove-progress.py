"""Remove snk's bottom progress rectangles while preserving its animation."""

import re
from pathlib import Path
from xml.etree import ElementTree


for path in Path("dist").glob("github-snake*.svg"):
    svg = path.read_text()
    svg = re.sub(
        r'<rect\b(?=[^>]*\bclass="u(?:\s[^"]*)?")[^>]*/>',
        "",
        svg,
    )
    root = ElementTree.fromstring(svg)
    assert not any("u" in node.get("class", "").split() for node in root.iter())
    assert any("s" in node.get("class", "").split() for node in root.iter())
    path.write_text(svg)
