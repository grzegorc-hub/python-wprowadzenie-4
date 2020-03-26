class C1:
    def meth1(self): self.__X = 88           # Teraz X jest moje
    def meth2(self): print(self.__X)         # Staje się _C1__X w I
class C2:
    def metha(self): self.__X = 99           # Jest też moje
    def methb(self): print(self.__X)         # Staje się _C2__X w I
class C3(C1, C2): pass

I = C3()                                     # Dwie zmienne X w I
I.meth1(); I.metha()
print(I.__dict__)
I.meth2(); I.methb()


def factory(aClass, *args):  # Krotka argumentów o zmiennej liczbie
    return aClass(*args)  # Wywołanie konstruktora klasy aClass l (lub apply w 2.6)

class Spam:
    def doit(self, message):
        print(message)

class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

object1 = factory(Spam)  # Utworzenie obiektu Spam
object2 = factory(Person, "Guido", "guru")  # Utworzenie obiektu Person

#################

assert 2==2



try:
    with open('data3') as myfile:
        for line in myfile:
            print(line)
except Exception as X:
    print("blad" + str(X.args))
else:
    print('bez bledu')
finally:
    print('koniec')

import sys

def action2():
   print(1 + [])                             # Wygenerowanie wyjątku TypeError

def action1():
   try:
      action2()
   except TypeError:                         # Najbardziej aktualna pasująca instrukcja try
      print(sys.exc_info())
      print('wewnętrzne try')

try:
   action1()
except TypeError:                            # Tutaj tylko jeśli action1 ponownie zgłasza wyjątek
   print('zewnętrzne try')

print(sys.exc_info())