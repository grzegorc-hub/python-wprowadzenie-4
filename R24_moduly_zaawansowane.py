# W Pythonie ukrywanie danych w modułach jest konwencją, a nie ograniczeniem składniowym.

# tylko przy uzyciu from *
from dir1.dir2.spam import *
print(name)
#print(_name) # blad
from dir1.dir2.spam import _name
print(_name)

# from __future__ import nazwa_opcji (Włączanie opcji z przyszłych wersji Pythona - domyslnie nowosci sa wylaczone)

# Każdy moduł ma wbudowany atrybut o nazwie __name__, który Python automatycznie ustawia w następujący sposób:
# - Jeśli plik jest wykonywany jako plik programu najwyższego poziomu, atrybut __name__ ustawiany jest po uruchomieniu na łańcuch znaków "__main__".
# - Jeśli plik jest importowany, atrybut __name__ jest zamiast tego ustawiany na nazwę modułu w formie znanej przez klienta.

def tester():
   print("Jest Gwiazdka w niebie...")
if __name__ == '__main__':                   # Tylko przy wykonywaniu
   tester()                                  # A nie przy importowaniu

