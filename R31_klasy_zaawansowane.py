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


def factory(aClass, *args):                 # funkcja generująca dowolne rodzaje obiektów. po co? klasa moze np. jeszcze nie istniec
    return aClass(*args)                    # Wywołanie konstruktora klasy aClass l (lub apply w 2.6)

def factory2(aClass, *args, **kwargs):
   return aClass(args, kwargs)

class Spam:
    def doit(self, message):
        print(message)

class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

object1 = factory(Spam)  # Utworzenie obiektu Spam
object2 = factory(Person, "Guido", "guru")  # Utworzenie obiektu Person


class C: pass
X = C()
print(type(C))
print(type(X))                              # wszyskie klasy sa typami
print(isinstance(C, object))                # wszystko dziedziczy po object
print(isinstance(X, object))


# Klasy w nowym stylu mają możliwość ograniczenia listy nazw, które można wykorzystać w instancjach.
# Służy do tego specjalny atrybut __slots__, któremu przypisuje się listę dostępnych nazw.
class limiter(object):
    __slots__ = ['age', 'name', 'job']

x = limiter()
#x.age                                  # Przed użyciem należy przypisać wartość
x.age = 40
print(x.age)
#x.ape = 1000                           # Nielegalne wywołanie: nazwa niezdefiniowana w __slots__
x.name = 'Bob'
print(x.name)


class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1
    @staticmethod
    def printNumInstances():
        print("Liczba utworzonych instancji: ", Spam.numInstances)

a = Spam()
b = Spam()
c = Spam()
Spam.printNumInstances()
c.printNumInstances()

# Metody instancji (domyslne)
# Metody statyczne - wywołuje się bez przekazywania obiektu instancji
# Metody klas - tak jak zwykłe metody, ale Python zamiast instancji przekazuje do nich klasę

# class MyClass:
#     def method(self):
#         return 'instance method called', self
#
#     @classmethod
#     def classmethod(cls):
#         return 'class method called', cls
#
#     @staticmethod
#     def staticmethod():
#         return 'static method called'


