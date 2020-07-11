# Nazwy bez zapisu kwalifikującego (na przykład X) związane są z zakresami.
# Nazwy z zapisem kwalifikującym (na przykład obiekt.X) wykorzystują przestrzenie nazw obiektów.

# przestrzenie nazw są tak naprawdę zaimplementowane jako słowniki i udostępniane za pomocą wbudowanego atrybutu __dict__.

# Plik manynames.py

X = 11                                     # Globalna zmienna/atrybut z modułu (X lub manynames.X)
def f():
   print(X)                                # Dostęp do zmiennej globalnej X (11)
def g():
   X = 22                                  # Zmienna lokalna (funkcji) — X ukrywa X z modułu
   print(X)
class C:
   X = 33                                  # Atrybut klasy (C.X)
   def m(self):
      X = 44                               # Zmienna lokalna metody (X)
      self.X = 55                          # Atrybut instancji (instance.X)


X = 11                                      # Zmienna globalna w module
def g1():
   print(X)                                 # Referencja do zmiennej globalnej modułu
def g2():
   global X
   X = 22                                   # Modyfikacja zmiennej globalnej modułu
def h1():
   X = 33                                   # Zmienna lokalna w funkcji
   def nested():
      print(X)                              # Referencja do zmiennej lokalnej w zakresie zawierającym
def h2():
   X = 33                                   # Zmienna lokalna w funkcji
   def nested():
      nonlocal X                            # Instrukcja Pythona 3.0
      X = 44                                # Modyfikacja zmiennej lokalnej w zakresie zawierającym



if __name__ == '__main__':
   print(X)                                 # 11: moduł (czyli manynames.X poza plikiem)
   f()                                      # 11: zmienna globalna
   g()                                      # 22: zmienna lokalna
   print(X)                                 # 11: zmienna modułu bez zmian
   obj = C()                                # Utworzenie instancji
   print(obj.X)                             # 33: zmienna klasy odziedziczona przez instancję
   obj.m()                                  # Dołączenie nazwy atrybutu X do instancji
   print(obj.X)                             # 55: instancja
   print(C.X)                               # 33: klasa (czyli obj.X jeśli nie ma X w instancji)
   #print(C.m.X)                            # PORAŻKA: widoczna tylko w metodzie
   #print(g.X)                              # PORAŻKA: widoczna tylko w funkcji