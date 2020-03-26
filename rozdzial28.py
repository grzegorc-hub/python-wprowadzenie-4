from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
   def method(self):
      print('w Super.method')                # Zachowanie domyślne
   def delegate(self):
      self.action()                          # Oczekuje zdefiniowania
   @abstractmethod
   def action(self):
       pass

class Inheritor(Super):                      # Odziedziczenie wszystkich metod
   pass

class Replacer(Super):                       # Całkowite zastąpienie metody method
   def method(self):
      print('w Replacer.method')

class Extender(Super):                       # Rozszerzenie działania metody method
   def method(self):
      print('początek Extender.method')
      Super.method(self)
      print('koniec Extender.method')

class Provider(Super):  # Uzupełnienie wymaganej metody
   def action(self):
       print('w Provider.action')

if __name__ == '__main__':
   # for klass in (Inheritor, Replacer, Extender):
   #     print('\n' + klass.__name__ + '...')
   #     klass().method()
   print('\nProvider...')
   x = Provider()
   x.delegate()


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