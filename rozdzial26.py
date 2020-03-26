class FirstClass:
    def setdata(self, val):
        self.data = val
    def display(self):
        print(self.data)

x = FirstClass()
y = FirstClass()
x.setdata('djifs')
y.setdata(8)
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

class ThirdClass(SecondClass):           # Dziedziczy po SecondClass
   def __init__(self, value):            # Przy "ThirdClass(value)"
      self.data = value
   def __add__(self, other):             # Przy "self + other"
      return ThirdClass(self.data + other)
   def __str__(self):                    # Przy "print(self)", "str()"
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