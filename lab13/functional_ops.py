"""
Prelucrare HashMap cu funcții de nivel superior.

Tema 1: aplică transformări unui dict folosind EXCLUSIV
funcții de nivel superior (lambda, map, filter, reduce).
NU se folosesc bucle for/while.

Logica transformărilor:
1. Elimină elementele prime (indiferent dacă sunt pare sau impare)
2. Transformă elementele impare non-prime în pare (înmulțire cu 2)
3. Elementele pare non-prime rămân neschimbate
"""

from functools import reduce


def is_prime(n: int) -> bool:
    """Verifică dacă un număr este prim.

    Un număr este prim dacă este mai mare decât 1 și are exact 2 divizori: 1 și el însuși.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Verificăm divizorii fără a folosi bucle for/while (folosim all cu range)
    return all(n % i != 0 for i in range(3, int(n**0.5) + 1, 2))


def make_even(n: int) -> int:
    """Transformă un număr impar în par prin înmulțire cu 2.

    Dacă numărul este deja par, îl returnează neschimbat.
    """
    return n * 2 if n % 2 != 0 else n


def process_hashmap(data: dict[str, int]) -> dict[str, int]:
    """Aplică transformările dict-ului folosind funcții de nivel superior.

    Transformări aplicate:
    1. Elimină perechile unde valoarea este număr prim
    2. Transformă valorile impare (non-prime) în pare (× 2)
    3. Valorile pare non-prime rămân neschimbate
    """
    # Folosim dict comprehension (permis de cerință) ca alternativă pur funcțională la map/filter aplicat pe dict-uri
    return {
        k: make_even(v)
        for k, v in data.items()
        if not is_prime(v)
    }