# Lab 13 — Python Programare Funcțională

## Descriere

Implementează transformări pe structuri de date folosind **exclusiv funcții de nivel superior** (lambda, map, filter, reduce) și un combinator de fișiere HTML cu expresii regulate.

## Structura proiectului

```
lab13/
  lab13/
    __init__.py
    functional_ops.py  ← operații funcționale pe dict (stub)
    html_combiner.py   ← combinator HTML (stub)
    main.py            ← entry point
  tests/
    __init__.py
    test_lab13.py      ← teste complete
  .github/workflows/classroom.yml
  pyproject.toml
  ASSIGNMENT.md
  README.md
```

## Cerințe

### Tema 1 — Prelucrare HashMap cu funcții de nivel superior

#### `functional_ops.py`

##### `is_prime(n: int) -> bool`

```python
assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(4) == False
assert is_prime(1) == False
```

##### `make_even(n: int) -> int`

Dacă n este impar → n × 2. Dacă par → n neschimbat.

```python
assert make_even(3) == 6
assert make_even(4) == 4
```

##### `process_hashmap(data: dict[str, int]) -> dict[str, int]`

Aplică simultan două transformări:
1. **Elimină** perechile cu valori prime
2. **Dublează** valorile impare non-prime

**IMPORTANT:** Implementare EXCLUSIV cu `map`, `filter`, `lambda`, dict comprehension sau `reduce`. **NU** se folosesc bucle `for`/`while`.

```python
process_hashmap({'a': 4, 'b': 7, 'c': 5})
# 4 par non-prim → rămâne 4
# 7 impar non-prim → devine 14
# 5 prim → eliminat
# Rezultat: {'a': 4, 'b': 14}
```

**Tabel de referință:**

| Valoare | Prim? | Impar? | Rezultat |
|---------|-------|--------|----------|
| 2 | DA | DA | eliminat |
| 3 | DA | DA | eliminat |
| 4 | NU | NU | 4 (nemodificat) |
| 5 | DA | DA | eliminat |
| 6 | NU | NU | 6 (nemodificat) |
| 7 | DA | DA | eliminat |
| 8 | NU | NU | 8 (nemodificat) |
| 9 | NU | DA | 18 (dublat) |
| 11 | DA | DA | eliminat |
| 49 | NU | DA | 98 (dublat) |

**Hint implementare:**
```python
# Pas 1: filtrează non-primele
non_prime_items = filter(lambda kv: not is_prime(kv[1]), data.items())
# Pas 2: aplică make_even pe valori
rezultat = {k: make_even(v) for k, v in non_prime_items}
```

### Tema 2 — Combinator HTML

#### `html_combiner.py`

##### `extract_body(html: str) -> str`

Extrage conținutul dintre `<body>` și `</body>`. Ignoră tag-urile `<html>`, `<head>...</head>`.

```python
extract_body("<html><body><p>test</p></body></html>")
# "<p>test</p>"

extract_body("<html><head><title>T</title></head><body><p>text</p></body></html>")
# "<p>text</p>"
```

**Hint:** Folosește `re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL)`.

##### `build_combined_html(bodies: list[str], source_names: list[str]) -> str`

Construiește HTML complet:
- `<head>` conține meta-descriere cu numele fișierelor sursă
- `<body>` conține toate body-urile concatenate

```python
build_combined_html(["<p>A</p>", "<p>B</p>"], ["a.html", "b.html"])
# "<!DOCTYPE html><html>
#   <head><meta name='description' content='Combinat din: a.html, b.html'></head>
#   <body><p>A</p><p>B</p></body>
# </html>"
```

##### `combine_files(input_paths: list[str], output_path: str) -> None`

Combină fișierele HTML:
1. Citește fiecare fișier
2. Extrage body-ul
3. Construiește documentul combinat
4. Scrie la `output_path`

```python
combine_files(["a.html", "b.html"], "combined.html")
```

## Exemple de utilizare

### Rulare demonstrație:
```bash
uv run python -m lab13.main
```

**Output exemplu:**
```
=== Operații funcționale pe HashMap ===

Numere prime din [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
  [2, 3, 5, 7, 11]

make_even aplicat pe [1..10]:
  [2, 2, 6, 4, 10, 6, 14, 8, 18, 10]

Input: {'a': 4, 'b': 7, 'c': 5, 'd': 9, 'e': 11, 'f': 6}
Output: {'a': 4, 'b': 14, 'd': 18, 'f': 6}

=== Combinator HTML ===

extract_body: '<p>Conținut</p>'
```

### Rulare teste:
```bash
uv run pytest
uv run pytest -v
```

## Tabel evaluare

| Cerință | Punctaj |
|---------|---------|
| `is_prime()` corect | 10p |
| `make_even()` corect | 5p |
| `process_hashmap()` — eliminare prime | 15p |
| `process_hashmap()` — dublare impare | 15p |
| `process_hashmap()` — fără bucle for/while | 10p |
| `extract_body()` corect | 15p |
| `build_combined_html()` — structură corectă | 15p |
| `combine_files()` — fișier creat corect | 15p |
| **Total** | **100p** |

## Resurse

- [functools.reduce — Python docs](https://docs.python.org/3/library/functools.html#functools.reduce)
- [map, filter — Python docs](https://docs.python.org/3/library/functions.html)
- [re — Python docs](https://docs.python.org/3/library/re.html)
- [Programare funcțională în Python](https://docs.python.org/3/howto/functional.html)
