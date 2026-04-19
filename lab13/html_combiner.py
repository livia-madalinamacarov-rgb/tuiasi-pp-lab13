"""
Combinator de fișiere HTML.

Tema 2: primește mai multe fișiere HTML, extrage body-urile
și le combină într-un singur fișier HTML.
"""

import re
from pathlib import Path


# TODO: Implementează funcția extract_body
def extract_body(html: str) -> str:
    """Extrage conținutul dintre tagurile <body> și </body>.

    Dacă nu există taguri body, returnează HTML-ul curățat de
    taguri <html>, <head>...</head>.

    Args:
        html: String-ul HTML din care se extrage body-ul.

    Returns:
        Conținutul interior al <body>, fără tagurile body înseși.

    Exemple:
        extract_body("<html><body><p>test</p></body></html>")
        # "<p>test</p>"

        extract_body("<html><head><title>T</title></head><body><p>text</p></body></html>")
        # "<p>text</p>"
    """
    raise NotImplementedError("De implementat")


# TODO: Implementează funcția build_combined_html
def build_combined_html(bodies: list[str], source_names: list[str]) -> str:
    """Construiește un document HTML care combină mai multe body-uri.

    Structura documentului rezultat:
    - <head> conține o descriere cu numele fișierelor sursă
    - <body> conține body-urile concatenate, separate vizual

    Args:
        bodies: Lista de conținuturi body extrase.
        source_names: Lista numelor fișierelor sursă (pentru descriere).

    Returns:
        Document HTML complet ca string.

    Exemplu:
        build_combined_html(["<p>A</p>", "<p>B</p>"], ["a.html", "b.html"])
        # "<!DOCTYPE html><html><head>...</head><body><p>A</p><p>B</p></body></html>"
        # <head> conține referințe la a.html și b.html
    """
    raise NotImplementedError("De implementat")


# TODO: Implementează funcția combine_files
def combine_files(input_paths: list[str], output_path: str) -> None:
    """Combină mai multe fișiere HTML într-un singur fișier.

    Pași:
    1. Citește fiecare fișier HTML din input_paths
    2. Extrage body-ul din fiecare
    3. Construiește documentul combinat
    4. Scrie rezultatul în output_path

    Args:
        input_paths: Lista căilor fișierelor HTML de intrare.
        output_path: Calea fișierului HTML de ieșire.
    """
    raise NotImplementedError("De implementat")
