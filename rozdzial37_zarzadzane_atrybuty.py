class Person:                            # W wersji 2.6 należy użyć (object)
   def __init__(self, name):
      self._name = name
   def getName(self):
      print('pobieranie...')
      return self._name
   def setName(self, value):
      print('modyfikacja...')
      self._name = value
   def delName(self):
      print('usunięcie...')
      del self._name
   name = property(getName, setName, delName, "Dokumentacja właściwości name")

bob = Person('Robert Zielony')           # bob ma zarządzany atrybut
print(bob.name)                          # Wykonuje getName
bob.name = 'Robert A. Zielony'           # Wykonuje setName
print(bob.name)
del bob.name                             # Wykonuje delName

anna = Person('Anna Czerwona')           # anna także dziedziczy właściwość
print(anna.name)
print(Person.name.__doc__)               # Lub help(Person.name)

print('-'*20)

# @dekorator
# def funkcja(argumenty): ...
#
# def funkcja(argumenty): ...
#    funkcja = dekorator(funkcja)

# np.
# class Person:
#    @property
#    def name(self): ...             #  name = property(name)
#
#    @name.setter
#    def name(self, value):          # name = name.setter(name)


class Cube:
   def __init__(self, x):
       self._x = x

   @property
   def x(self):
       "Some doc"
       print('pobieranie...')
       return self._x + 2

   @x.setter
   def x(self, value):
       print('modyfikacja...')
       self._x = value - 1

   @x.deleter
   def x(self):
       print('usunięcie...')
       del self._x

c = Cube(5)
print(c.x)
c.x = 10
print(c.x)
del c.x

print('-' * 20)

# TODO: deskryptory