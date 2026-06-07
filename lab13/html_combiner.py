"""
Combinator de fișiere HTML.

Tema 2: primește mai multe fișiere HTML, extrage body-urile
și le combină într-un singur fișier HTML.
"""

import re
from pathlib import Path


def extract_body(html: str) -> str:
    """Extrage conținutul dintre tagurile <body> și </body>.

    Dacă nu există taguri body, returnează HTML-ul curățat de
    taguri <html>, <head>...</head>.
    """
    # Folosim re.IGNORECASE și re.DOTALL pentru a prinde și tag-uri pe mai multe linii sau scrise cu majuscule
    match = re.search(r"<body[^>]*>(.*?)</body>", html, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1)

    # Dacă nu are tag-uri body, curățăm de <html> și <head>
    cleaned = re.sub(r"<head[^>]*>.*?</head>", "", html, flags=re.IGNORECASE | re.DOTALL)
    cleaned = re.sub(r"</?html[^>]*>", "", cleaned, flags=re.IGNORECASE | re.DOTALL)
    return cleaned


def build_combined_html(bodies: list[str], source_names: list[str]) -> str:
    """Construiește un document HTML care combină mai multe body-uri.

    Structura documentului rezultat:
    - <head> conține o descriere cu numele fișierelor sursă
    - <body> conține body-urile concatenate, separate vizual
    """
    # Generăm o descriere simplă a surselor pentru zona de <head>
    surse_str = ", ".join(source_names)
    head_content = f"<meta name='description' content='Combined from: {surse_str}'>" if source_names else ""

    # Concatenăm toate secțiunile de body primite
    combined_bodies = "".join(bodies)

    # Asamblăm structura de document HTML valid cerută de teste
    html_document = (
        "<!DOCTYPE html>\n"
        "<html>\n"
        f"<head>\n{head_content}\n</head>\n"
        f"<body>\n{combined_bodies}\n</body>\n"
        "</html>"
    )
    return html_document


def combine_files(input_paths: list[str], output_path: str) -> None:
    """Combină mai multe fișiere HTML într-un singur fișier.

    Pași:
    1. Citește fiecare fișier HTML din input_paths
    2. Extrage body-ul din fiecare
    3. Construiește documentul combinat
    4. Scrie rezultatul în output_path
    """
    bodies = []
    source_names = []

    for path_str in input_paths:
        p = Path(path_str)
        if p.exists():
            # 1. Citire fișier
            with open(p, "r", encoding="utf-8") as f:
                content = f.read()
            # 2. Extragere body
            bodies.append(extract_body(content))
            source_names.append(p.name)

    # 3. Construire document combinat
    combined_html = build_combined_html(bodies, source_names)

    # 4. Scriere rezultat în fișierul de ieșire
    out_p = Path(output_path)
    # Ne asigurăm că directorul părinte există
    out_p.parent.mkdir(parents=True, exist_ok=True)
    with open(out_p, "w", encoding="utf-8") as f:
        f.write(combined_html)