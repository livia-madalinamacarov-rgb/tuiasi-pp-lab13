"""
Entry point pentru demonstrarea programării funcționale.

Utilizare:
    uv run python -m lab13.main
"""

import tempfile
import os
from lab13.functional_ops import is_prime, make_even, process_hashmap
from lab13.html_combiner import extract_body, build_combined_html, combine_files


def main() -> None:
    """Demonstrează funcționalitățile de programare funcțională."""
    print("=== Operații funcționale pe HashMap ===\n")

    # Testare is_prime
    numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    prime = list(filter(is_prime, numere))
    print(f"Numere prime din {numere}:")
    print(f"  {prime}\n")

    # Testare make_even
    print("make_even aplicat pe [1..10]:")
    rezultate = list(map(make_even, range(1, 11)))
    print(f"  {rezultate}\n")

    # Testare process_hashmap
    data = {"a": 4, "b": 7, "c": 5, "d": 9, "e": 11, "f": 6}
    print(f"Input: {data}")
    rezultat = process_hashmap(data)
    print(f"Output: {rezultat}")
    print("(primele eliminate, impare → × 2)\n")

    print("=== Combinator HTML ===\n")

    # Testare extract_body
    html = "<html><head><title>Test</title></head><body><p>Conținut</p></body></html>"
    body = extract_body(html)
    print(f"extract_body: {repr(body)}\n")

    # Testare combine_files
    with tempfile.TemporaryDirectory() as tmpdir:
        fisier1 = os.path.join(tmpdir, "a.html")
        fisier2 = os.path.join(tmpdir, "b.html")
        output = os.path.join(tmpdir, "combinat.html")

        with open(fisier1, "w") as f:
            f.write("<html><body><p>Primul document</p></body></html>")
        with open(fisier2, "w") as f:
            f.write("<html><body><h2>Al doilea document</h2></body></html>")

        combine_files([fisier1, fisier2], output)

        with open(output) as f:
            print("Fișier combinat:")
            print(f.read())


if __name__ == "__main__":
    main()
