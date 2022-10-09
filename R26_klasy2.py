# Instrukcja class tworzy obiekt klasy i przypisuje go do nazwy (class jest instrukcja wykonywalna,
# kiedy Python do niej dojdzie, generuje nowy obietk klasy (tak jek np. obiekt funkcji)
# Przypisania wewnątrz instrukcji class tworzą atrybuty klasy
# Atrybuty klasy udostępniają stan obiektu oraz jego zachowanie (wspołdzielone przez wszystkie instancje utworzone z tej klasy)

# Wywołanie obiektu klasy w sposób podobny do wywołania funkcji tworzy nowy obiekt instancji.
# Każdy obiekt instancji dziedziczy atrybuty klasy oraz otrzymuje własną przestrzeń nazw.
# Przypisania do atrybutów self w metodach tworzą atrybuty instancji.

class FirstClass:
    a = 44
    def setdata(self, val):
        self.data = val
    def display(self):
        print(self.data, self.a)

x = FirstClass()
y = FirstClass()

print(type(FirstClass))
print(type(x))
print((x.a))

x.setdata('djifs')
y.setdata(8)
x.a = 55
x.display()
y.display()

x.data = "sss"
x.display()
x.data2 = 55

class SecondClass(FirstClass):
    def display(self):
        print('value = %s' % self.data)

z = SecondClass()
z.setdata(44)
z.display()

class ThirdClass(SecondClass):               # Dziedziczy po SecondClass
   def __init__(self, value):                # Przy "ThirdClass(value)"
      self.data = value
   def __add__(self, other):                 # Przy "self + other"
      return ThirdClass(self.data + other)
   def __str__(self):                        # Przy "print(self)", "str()"
      return '[ThirdClass: %s]' % self.data
   def mul(self, other):
      self.data *= other

a = ThirdClass('abc')
a.display()
print(a)
b = a + 'xyz'
b.display()
a.mul(3)
print(a)

def upperName(self):
    print(self.data.upper())

upperName(a)
ThirdClass.method = upperName
a.method()


class rec: pass
pers1 = rec()                             # Informacje zapisane w instancjach
pers1.name = 'mel'
pers1.job = 'instruktor'
pers1.age = 40

pers2 = rec()
pers2.name = 'vls'
pers2.job = 'programista'

print( pers1.name, pers2.name )