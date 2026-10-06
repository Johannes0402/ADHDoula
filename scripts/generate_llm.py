#!/usr/bin/env python3
"""Maak LLM-spiegels, llms.txt, llms-full.txt en sitemap.xml uit de HTML.

HTML is de bron voor de paginaspiegels. ai-knowledge-pack.md blijft met de hand.
Een profiel-link (rel=me) op over-mij.html moet ook in dat kennisbestand staan.

Gebruik:
  python3 scripts/generate_llm.py
  python3 scripts/generate_llm.py --check
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://www.adhdoula.nl"
KNOWLEDGE = ROOT / "ai-knowledge-pack.md"
INTRO = Path(__file__).resolve().parent / "llms-intro.md"

# Volgorde in sitemap, llms.txt en llms-full.txt.
PAGES = [
    ("index.html", "Home"),
    ("geboorte.html", "Geboorte"),
    ("postpartum.html", "Postpartum"),
    ("over-mij.html", "Over Kayleigh"),
    ("wel-en-niet.html", "Wel en niet"),
    ("werkgebied.html", "Werkgebied"),
    ("vragen.html", "Vragen"),
    ("kennismaking.html", "Kennismaking"),
    ("bericht-verstuurd.html", "Bericht verstuurd"),
]

BLOCK = {"h1", "h2", "h3", "h4", "p", "ul", "ol", "li", "section", "div", "article", "main", "nav"}
VOID = {"br", "img", "hr", "meta", "link", "input", "source", "wbr"}
SKIP = {"script", "style", "noscript", "svg"}


class Node:
    def __init__(self, tag: str, attrs: dict[str, str]) -> None:
        self.tag = tag
        self.attrs = attrs
        self.children: list[Node | str] = []


class MainTree(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.main: Node | None = None
        self.stack: list[Node] = []
        self.skip = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        ad = {key: value or "" for key, value in attrs}
        if tag == "main" and self.main is None:
            self.main = Node("main", ad)
            self.stack = [self.main]
            return
        if not self.stack:
            return
        if tag in SKIP:
            self.skip += 1
            return
        if self.skip:
            return
        node = Node(tag, ad)
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_endtag(self, tag: str) -> None:
        if tag in SKIP and self.skip:
            self.skip -= 1
            return
        if tag == "main" and self.stack:
            self.stack = []
            return
        if self.stack and self.stack[-1].tag == tag:
            self.stack.pop()

    def handle_data(self, data: str) -> None:
        if self.stack and not self.skip and data:
            self.stack[-1].children.append(data)


def classes(node: Node) -> set[str]:
    return set(node.attrs.get("class", "").split())


def absolute(href: str) -> str:
    href = href.strip()
    if not href or href.startswith("#"):
        return ""
    if href.startswith(("mailto:", "tel:", "http://", "https://")):
        return href
    if href.startswith("/"):
        return ORIGIN + href
    return ORIGIN + "/" + href


def collapse(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def inline(nodes: list[Node | str]) -> str:
    parts: list[str] = []
    for child in nodes:
        if isinstance(child, str):
            parts.append(collapse(child))
            continue
        if "crumbs" in classes(child) or child.tag == "img":
            continue
        if child.tag == "a":
            label = inline(child.children).strip()
            href = absolute(child.attrs.get("href", ""))
            parts.append(f"[{label}]({href})" if label and href else label)
            continue
        if child.tag == "br":
            parts.append("\n")
            continue
        parts.append(inline(child.children))
    return "".join(parts).strip()


def render(node: Node, out: list[str], skip_lede: bool) -> None:
    if classes(node) & {"crumbs", "kicker"} or node.tag in ("img", "script", "style", "h1"):
        return
    if node.tag in ("h2", "h3", "h4"):
        text = inline(node.children)
        if text:
            out.append(f"{'#' * int(node.tag[1])} {text}")
            out.append("")
        return
    if node.tag == "p":
        if skip_lede and "lede" in classes(node):
            return
        text = inline(node.children)
        if text:
            out.append(text)
            out.append("")
        return
    if node.tag in ("ul", "ol"):
        items = [child for child in node.children if isinstance(child, Node) and child.tag == "li"]
        for index, item in enumerate(items, 1):
            text = inline(item.children)
            if not text:
                continue
            prefix = f"{index}. " if node.tag == "ol" else "- "
            out.append(prefix + text)
        if items:
            out.append("")
        return
    if node.tag == "a":
        text = inline([node])
        if text:
            out.append(text)
            out.append("")
        return
    for child in node.children:
        if isinstance(child, Node):
            render(child, out, skip_lede)


def meta(html: str, name: str) -> str:
    match = re.search(
        rf'<meta[^>]+name="{re.escape(name)}"[^>]+content="([^"]*)"',
        html,
    )
    if match:
        return match.group(1).strip()
    match = re.search(
        rf'<meta[^>]+content="([^"]*)"[^>]+name="{re.escape(name)}"',
        html,
    )
    return match.group(1).strip() if match else ""


def canonical(html: str, filename: str) -> str:
    match = re.search(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"', html)
    if match:
        return match.group(1).strip()
    if filename == "index.html":
        return ORIGIN + "/"
    return ORIGIN + "/" + filename


def markdown_name(filename: str) -> str:
    return "index.md" if filename == "index.html" else Path(filename).with_suffix(".md").name


def first_text(tree: Node, tag: str, class_name: str | None = None) -> str:
    found: list[str] = []

    def walk(node: Node) -> None:
        if found:
            return
        if node.tag == tag and (class_name is None or class_name in classes(node)):
            text = inline(node.children)
            if text:
                found.append(text)
                return
        for child in node.children:
            if isinstance(child, Node):
                walk(child)

    walk(tree)
    return found[0] if found else ""


def page_markdown(filename: str, html: str) -> str:
    parser = MainTree()
    parser.feed(html)
    if parser.main is None:
        raise SystemExit(f"{filename}: geen <main>")
    heading = first_text(parser.main, "h1")
    lede = first_text(parser.main, "p", "lede") or meta(html, "description")
    if not heading or not lede:
        raise SystemExit(f"{filename}: H1 of intro ontbreekt")
    url = canonical(html, filename)
    mirror = ORIGIN + "/" + markdown_name(filename)
    body: list[str] = []
    render(parser.main, body, skip_lede=True)
    text = "\n".join(
        [
            f"# {heading}",
            "",
            f"> {lede}",
            "",
            f"- URL: {url}",
            "- Language: nl",
            f"- Markdown: {mirror}",
            "",
            "\n".join(body).strip(),
            "",
        ]
    )
    return text.replace("\n\n\n", "\n\n")


def profiles(html: str) -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    for href, label in re.findall(
        r'<a[^>]*rel="me"[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
        html,
        flags=re.I | re.S,
    ):
        clean = re.sub(r"<[^>]+>", "", label)
        clean = collapse(clean).strip()
        found.append((clean or href, href.strip()))
    if not found:
        raise SystemExit("over-mij.html: geen profiel-link met rel=me")
    pack = KNOWLEDGE.read_text(encoding="utf-8")
    missing = [href for _, href in found if href not in pack]
    if missing:
        raise SystemExit(
            "Deze profiel-URL's staan op Over Kayleigh, maar niet in ai-knowledge-pack.md: "
            + ", ".join(missing)
        )
    return found


def llms_txt(pages: list[tuple[str, str, str]], profile_links: list[tuple[str, str]]) -> str:
    intro = INTRO.read_text(encoding="utf-8").rstrip()
    lines = [intro, ""]
    for label, href in profile_links:
        lines.append(f"**{label}:** {href}")
    lines.append("")
    lines.append("## Pagina's")
    lines.append("")
    lines.append(
        "Markdown-spiegels (llmstxt.org): hetzelfde pad plus `.md`. Home is `/index.md`. HTML blijft de canonieke URL."
    )
    lines.append("")
    for label, mirror, description in pages:
        lines.append(f"- [{label}]({mirror}): {description}")
    lines.append("")
    return "\n".join(lines)


def llms_full(mirrors: list[str]) -> str:
    parts = [
        "# ADHDoula — volledige tekst\n\nLanguage: nl\nCanonieke site: https://www.adhdoula.nl/\nKennisbestand: https://www.adhdoula.nl/ai-knowledge-pack.md\n",
        KNOWLEDGE.read_text(encoding="utf-8").strip() + "\n",
        *mirrors,
    ]
    return "\n\n---\n\n".join(part.strip() + "\n" for part in parts)


def sitemap(stamps: list[tuple[str, str]]) -> str:
    rows = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lastmod in stamps:
        rows.append(f"  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod></url>")
    rows.append("</urlset>")
    rows.append("")
    return "\n".join(rows)


def build() -> dict[Path, str]:
    html_names = sorted(path.name for path in ROOT.glob("*.html"))
    expected = sorted(name for name, _label in PAGES)
    if html_names != expected:
        raise SystemExit(
            "HTML-pagina's en PAGES in scripts/generate_llm.py wijken af.\n"
            f"Op schijf: {', '.join(html_names)}\n"
            f"In PAGES: {', '.join(expected)}"
        )
    outputs: dict[Path, str] = {}
    mirrors: list[str] = []
    index_rows: list[tuple[str, str, str]] = []
    stamps: list[tuple[str, str]] = []
    profile_links: list[tuple[str, str]] = []
    for filename, label in PAGES:
        path = ROOT / filename
        html = path.read_text(encoding="utf-8")
        if filename == "over-mij.html":
            profile_links = profiles(html)
        document = page_markdown(filename, html)
        outputs[ROOT / markdown_name(filename)] = document
        mirrors.append(document)
        url = canonical(html, filename)
        description = meta(html, "description")
        if not description:
            raise SystemExit(f"{filename}: meta description ontbreekt")
        if "noindex" not in html:
            index_rows.append((label, ORIGIN + "/" + markdown_name(filename), description))
            lastmod = datetime.fromtimestamp(path.stat().st_mtime).date().isoformat()
            stamps.append((url, lastmod))
    outputs[ROOT / "llms.txt"] = llms_txt(index_rows, profile_links)
    outputs[ROOT / "llms-full.txt"] = llms_full(mirrors)
    outputs[ROOT / "sitemap.xml"] = sitemap(stamps)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(description="Werk LLM-bestanden en de sitemap bij vanuit de HTML.")
    parser.add_argument("--check", action="store_true", help="Stop met code 1 als een gegenereerd bestand achterloopt.")
    args = parser.parse_args()
    outputs = build()
    stale: list[str] = []
    for path, text in outputs.items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != text:
            stale.append(path.name)
            if not args.check:
                path.write_text(text, encoding="utf-8")
    if args.check and stale:
        print("Achterlopend: " + ", ".join(stale), file=sys.stderr)
        print("Draai: python3 scripts/generate_llm.py", file=sys.stderr)
        return 1
    if stale:
        print("Bijgewerkt: " + ", ".join(stale))
    else:
        print("LLM-bestanden en sitemap zijn al gelijk aan de HTML.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
