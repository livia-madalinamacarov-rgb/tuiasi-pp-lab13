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


# TODO: Implementează funcția is_prime
def is_prime(n: int) -> bool:
    """Verifică dacă un număr este prim.

    Un număr este prim dacă este mai mare decât 1 și are exact 2 divizori: 1 și el însuși.

    Args:
        n: Numărul de verificat.

    Returns:
        True dacă n este prim, False altfel.

    Exemple:
        is_prime(2) == True
        is_prime(3) == True
        is_prime(4) == False
        is_prime(1) == False
        is_prime(0) == False
    """
    raise NotImplementedError("De implementat")


# TODO: Implementează funcția make_even
def make_even(n: int) -> int:
    """Transformă un număr impar în par prin înmulțire cu 2.

    Dacă numărul este deja par, îl returnează neschimbat.

    Args:
        n: Numărul de transformat.

    Returns:
        n * 2 dacă n este impar, altfel n.

    Exemple:
        make_even(3) == 6
        make_even(4) == 4
        make_even(7) == 14
    """
    raise NotImplementedError("De implementat")


# TODO: Implementează funcția process_hashmap
def process_hashmap(data: dict[str, int]) -> dict[str, int]:
    """Aplică transformările dict-ului folosind funcții de nivel superior.

    Transformări aplicate:
    1. Elimină perechile unde valoarea este număr prim
    2. Transformă valorile impare (non-prime) în pare (× 2)
    3. Valorile pare non-prime rămân neschimbate

    IMPORTANT: Implementarea NU trebuie să conțină bucle for/while.
    Folosește exclusiv: map, filter, lambda, dict comprehension, reduce.

    Args:
        data: Dict-ul de procesat {cheie: valoare_int}.

    Returns:
        Dict nou cu transformările aplicate.

    Exemple:
        process_hashmap({'a': 4, 'b': 7, 'c': 5})
        # 4 par non-prim → rămâne 4
        # 7 impar non-prim → devine 14
        # 5 prim → eliminat
        # Rezultat: {'a': 4, 'b': 14}

        process_hashmap({'x': 3, 'y': 6, 'z': 11})
        # 3 prim → eliminat
        # 6 par non-prim → rămâne 6
        # 11 prim → eliminat
        # Rezultat: {'y': 6}
    """
    raise NotImplementedError("De implementat")
