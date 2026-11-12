#!/usr/bin/env python3
"""Check HTML2PDF local references and embedded JavaScript syntax."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


class HTMLValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []
        self.scripts = []
        self.current_script = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        key = "src" if tag in {"script", "img", "source", "iframe"} else "href"
        if attrs.get(key):
            self.references.append(attrs[key])
        if tag == "script":
            script_type = attrs.get("type", "").lower()
            if "src" not in attrs and script_type in {"", "text/javascript", "application/javascript", "module"}:
                self.current_script = []
            else:
                self.current_script = None

    def handle_data(self, data):
        if self.current_script is not None:
            self.current_script.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self.current_script is not None:
            self.scripts.append("".join(self.current_script))
            self.current_script = None


def main():
    page = ROOT / "index.html"
    parser = HTMLValidator()
    parser.feed(page.read_text(encoding="utf-8"))

    missing = []
    for reference in parser.references:
        parsed = urlsplit(reference)
        if parsed.scheme or not parsed.path:
            continue
        target = (ROOT / unquote(parsed.path)).resolve()
        if not target.exists():
            missing.append(reference)
    if missing:
        raise SystemExit("Missing local references: " + ", ".join(missing))

    node = shutil.which("node")
    if parser.scripts and not node:
        raise SystemExit("Node.js is required to syntax-check inline JavaScript.")

    with tempfile.TemporaryDirectory() as temp_dir:
        for index, source in enumerate(parser.scripts, start=1):
            if not source.strip():
                continue
            script_path = Path(temp_dir) / f"inline-{index}.js"
            script_path.write_text(source, encoding="utf-8")
            subprocess.run([node, "--check", str(script_path)], check=True)

    print(f"Validated index.html, {len(parser.scripts)} inline script(s), and local references.")


if __name__ == "__main__":
    main()
