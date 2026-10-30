from shutil import copy2 
from pathlib import Path 
from  BLOCKS.monad import M


def card(title, description):
    return M(
               M(title, t="h2"), 
               M(description, t="p"), 
               t="article"
            )


def meta(**aa):
    return M(t="meta", v=True, **aa)

def stylesheet(href):
    return M(t="link", v=True, rel="stylesheet", href=href)

def head(title): 
    header =  M(
            meta(charset="utf-8"), 
            meta(name="viewport", content="width=device-width, initial-scale=1"), 
            stylesheet("style.css"),
            t="head"
            )
    header.mon(title, t="title")
    return header

def build(root, * ,title="3F", css="", out="dest"):
    folder = Path(out)
    folder.mkdir(parents=True, exist_ok=True) 
    
    font = (Path(__file__).resolve().parent / "ASSETS"/ "FONTS" / "NBI.woff") 
    copy2(font, folder / font.name) 

    page = M(t="html", lang="en")
    page = M(head(title), M(root, t="body"), t="html", lang="en")

    document = "<!doctype html>\n" + page.render()

    
    (folder / "index.html").write_text(document, encoding="utf-8")
    (folder / "style.css").write_text(css, encoding="utf-8")

    return folder / "index.html"




theme = """

body {
    margin: 2rem; 
    background: #00f; 
    color: #fff; 
} 
@font-face {
    font-family: "NBI";
    src: url("NBI.woff") format("woff");
    font-weight: 400;
    font-style: normal;
    font-display: swap;
}

:root {
    --font-default: "NBI", sans-serif;
}

html {
    font-family: var(--font-default);
}

*, *::before, *::after {
    font-family: inherit;
}
"""

page = M(t = "main")
page.mon("3f", t="h1")
page.mon(card("fractal.fish", " a page is a composition isnt int? "))

out = build(page, title="3F/hello", css=theme)

print(f"built {out}")
