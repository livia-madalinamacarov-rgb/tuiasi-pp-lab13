"""
Teste pentru Lab 13 — Python Programare Funcțională.

Testele acoperă:
- is_prime, make_even, process_hashmap
- extract_body, build_combined_html, combine_files
"""

import os
import pytest

from lab13.functional_ops import is_prime, make_even, process_hashmap
from lab13.html_combiner import extract_body, build_combined_html, combine_files


class TestFunctionalOps:
    """Teste pentru operații funcționale pe HashMap."""

    # ── is_prime ──────────────────────────────────────────────────────────────

    def test_is_prime_doi(self) -> None:
        """2 este prim."""
        assert is_prime(2) is True

    def test_is_prime_trei(self) -> None:
        """3 este prim."""
        assert is_prime(3) is True

    def test_is_prime_cinci(self) -> None:
        """5 este prim."""
        assert is_prime(5) is True

    def test_is_prime_unsprezece(self) -> None:
        """11 este prim."""
        assert is_prime(11) is True

    def test_is_prime_unu_nu_este_prim(self) -> None:
        """1 nu este prim."""
        assert is_prime(1) is False

    def test_is_prime_zero_nu_este_prim(self) -> None:
        """0 nu este prim."""
        assert is_prime(0) is False

    def test_is_prime_patru_nu_este_prim(self) -> None:
        """4 nu este prim."""
        assert is_prime(4) is False

    def test_is_prime_sase_nu_este_prim(self) -> None:
        """6 nu este prim."""
        assert is_prime(6) is False

    def test_is_prime_noua_nu_este_prim(self) -> None:
        """9 nu este prim (9 = 3×3)."""
        assert is_prime(9) is False

    # ── make_even ─────────────────────────────────────────────────────────────

    def test_make_even_impar(self) -> None:
        """Numărul impar este dublat."""
        assert make_even(3) == 6

    def test_make_even_par(self) -> None:
        """Numărul par rămâne neschimbat."""
        assert make_even(4) == 4

    def test_make_even_sapte(self) -> None:
        """7 → 14."""
        assert make_even(7) == 14

    def test_make_even_zero(self) -> None:
        """0 (par) rămâne 0."""
        assert make_even(0) == 0

    def test_make_even_unu(self) -> None:
        """1 (impar) → 2."""
        assert make_even(1) == 2

    # ── process_hashmap ───────────────────────────────────────────────────────

    def test_process_hashmap_simplu(self) -> None:
        """Test de bază: prim eliminat, impar dublat, par rămâne."""
        rezultat = process_hashmap({"a": 4, "b": 7, "c": 5})
        # 4 par non-prim → rămâne 4
        # 7 impar non-prim → devine 14
        # 5 prim → eliminat
        assert rezultat == {"a": 4, "b": 14}

    def test_process_hashmap_toate_prime_eliminate(self) -> None:
        """Toate valorile prime sunt eliminate."""
        rezultat = process_hashmap({"a": 2, "b": 3, "c": 5, "d": 7})
        assert rezultat == {}

    def test_process_hashmap_fara_prime(self) -> None:
        """Fără valori prime: impare dublate, pare nemodificate."""
        rezultat = process_hashmap({"a": 4, "b": 9, "c": 6})
        # 4 par → 4; 9 impar non-prim → 18; 6 par → 6
        assert rezultat == {"a": 4, "b": 18, "c": 6}

    def test_process_hashmap_dict_gol(self) -> None:
        """Dict gol returnează dict gol."""
        assert process_hashmap({}) == {}

    def test_process_hashmap_toate_pare_non_prime(self) -> None:
        """Valorile pare non-prime rămân neschimbate."""
        rezultat = process_hashmap({"a": 4, "b": 6, "c": 8, "d": 9})
        assert rezultat["a"] == 4
        assert rezultat["b"] == 6
        assert rezultat["c"] == 8
        # 9 impar non-prim → 18
        assert rezultat["d"] == 18

    def test_process_hashmap_valori_mari(self) -> None:
        """Valori mai mari sunt tratate corect."""
        # 49 = 7×7, impar, non-prim → 98
        # 47 este prim → eliminat
        # 48 par non-prim → 48
        rezultat = process_hashmap({"a": 49, "b": 47, "c": 48})
        assert "b" not in rezultat  # 47 prim eliminat
        assert rezultat["a"] == 98  # 49 impar non-prim → 98
        assert rezultat["c"] == 48  # 48 par non-prim → 48

    def test_process_hashmap_returneaza_dict(self) -> None:
        """process_hashmap returnează un dict."""
        assert isinstance(process_hashmap({"a": 1}), dict)

    def test_process_hashmap_nu_modifica_inputul(self) -> None:
        """Input-ul original nu este modificat."""
        data = {"a": 4, "b": 7, "c": 5}
        original = dict(data)
        process_hashmap(data)
        assert data == original


class TestHtmlCombiner:
    """Teste pentru combinatorul de fișiere HTML."""

    # ── extract_body ──────────────────────────────────────────────────────────

    def test_extract_body_simplu(self) -> None:
        """Extrage conținutul din body simplu."""
        html = "<html><body><p>test</p></body></html>"
        rezultat = extract_body(html)
        assert "<p>test</p>" in rezultat

    def test_extract_body_fara_taguri_body(self) -> None:
        """extract_body returnează un string (chiar dacă nu există body)."""
        html = "<p>text simplu</p>"
        rezultat = extract_body(html)
        assert isinstance(rezultat, str)
        assert "text simplu" in rezultat

    def test_extract_body_cu_head(self) -> None:
        """head-ul este eliminat din rezultat."""
        html = "<html><head><title>Titlu</title></head><body><p>text</p></body></html>"
        rezultat = extract_body(html)
        assert "text" in rezultat
        # head-ul sau title nu trebuie să apară în body
        assert "<title>" not in rezultat

    def test_extract_body_nu_include_taguri_body(self) -> None:
        """Tagurile <body> și </body> nu apar în rezultat."""
        html = "<html><body><p>conținut</p></body></html>"
        rezultat = extract_body(html)
        assert "<body>" not in rezultat
        assert "</body>" not in rezultat

    def test_extract_body_returneaza_string(self) -> None:
        """extract_body returnează un string."""
        assert isinstance(extract_body("<html><body></body></html>"), str)

    def test_extract_body_body_gol(self) -> None:
        """Body gol returnează string gol sau whitespace."""
        rezultat = extract_body("<html><body></body></html>")
        assert rezultat.strip() == ""

    # ── build_combined_html ───────────────────────────────────────────────────

    def test_build_combined_html_contine_body_uri(self) -> None:
        """HTML combinat conține ambele body-uri."""
        rezultat = build_combined_html(["<p>A</p>", "<p>B</p>"], ["a.html", "b.html"])
        assert "<p>A</p>" in rezultat
        assert "<p>B</p>" in rezultat

    def test_build_combined_html_contine_nume_surse(self) -> None:
        """HTML combinat conține numele fișierelor sursă (în head)."""
        rezultat = build_combined_html(["<p>text</p>"], ["sursa.html"])
        assert "sursa.html" in rezultat

    def test_build_combined_html_structura_html(self) -> None:
        """Rezultatul este un document HTML structurat."""
        rezultat = build_combined_html(["<p>test</p>"], ["test.html"])
        # Trebuie să aibă cel puțin taguri html sau body
        assert "<html>" in rezultat or "<!DOCTYPE" in rezultat

    def test_build_combined_html_liste_goale(self) -> None:
        """Liste goale produc un HTML minimal valid."""
        rezultat = build_combined_html([], [])
        assert isinstance(rezultat, str)
        assert len(rezultat) > 0

    # ── combine_files ─────────────────────────────────────────────────────────

    def test_combine_files_creaza_fisier(self, tmp_path) -> None:
        """combine_files creează fișierul de ieșire."""
        fisier1 = tmp_path / "a.html"
        fisier1.write_text("<html><body><p>A</p></body></html>", encoding="utf-8")

        output = str(tmp_path / "out.html")
        combine_files([str(fisier1)], output)

        assert os.path.exists(output)

    def test_combine_files_contine_continuturile(self, tmp_path) -> None:
        """Fișierul combinat conține conținuturile ambelor fișiere."""
        fisier1 = tmp_path / "a.html"
        fisier2 = tmp_path / "b.html"
        fisier1.write_text("<html><body><p>Primul</p></body></html>", encoding="utf-8")
        fisier2.write_text("<html><body><p>Al doilea</p></body></html>", encoding="utf-8")

        output = str(tmp_path / "out.html")
        combine_files([str(fisier1), str(fisier2)], output)

        with open(output, encoding="utf-8") as f:
            continut = f.read()

        assert "Primul" in continut
        assert "Al doilea" in continut

    def test_combine_files_contine_nume_surse(self, tmp_path) -> None:
        """Fișierul combinat menționează sursele."""
        fisier = tmp_path / "sursa.html"
        fisier.write_text("<html><body><p>text</p></body></html>", encoding="utf-8")

        output = str(tmp_path / "out.html")
        combine_files([str(fisier)], output)

        with open(output, encoding="utf-8") as f:
            continut = f.read()

        assert "sursa.html" in continut

    def test_combine_files_lista_goala(self, tmp_path) -> None:
        """combine_files cu listă goală creează fișier HTML valid."""
        output = str(tmp_path / "out.html")
        combine_files([], output)
        assert os.path.exists(output)
        with open(output, encoding="utf-8") as f:
            continut = f.read()
        assert len(continut) > 0
