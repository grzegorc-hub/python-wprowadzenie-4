"""
Dokumentacja modułu
Tutaj jego opis
"""

spam = 40


def square(x):
    """
    Dokumentacja funkcji
    Możemy wziąć Pańską wątrobę?
    """
    return x ** 2  # Kwadrat


class Employee:
    "dokumentacja klasy"
    pass


if __name__ == '__main__':
    print(square(4))
    print(square.__doc__)
    print(Employee.__doc__)
    print(globals().keys())
    print(globals()['__doc__'])
