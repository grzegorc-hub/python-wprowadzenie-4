# instance.attribute would become getattr(instance, attribute_name)
class Foo:
    def __init__(self):
        print("__init__")
        self.x = 9
    def __getattr__(self, item):          # only gets called for attributes that don't actually exist
        print("__getattr__", item)
    def __setattr__(self, key, value):
        print("__setattr__", key, value)
        object.__setattr__(self, key, value)
    def __getattribute__(self, item):     # when attribute exists
        print("__getattribute__", item)
        return object.__getattribute__(self, item)

obj = Foo()
print(obj.x)
#obj.y = 11
print(obj.y)

############################


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

########################


class Descriptorr(object):
    def __get__(self, instance, owner):
        print(self, instance, owner, sep='-')

class Subject:
    attr = Descriptorr()                 # Instancja klasy Descriptor jest atrybutem klasy

X = Subject()
print(X.attr)
print()
print(Subject.attr)
print()


class Name:                            # W Pythonie 2.6 należy użyć (object)
   "Dokumentacja deskryptora name"
   def __get__(self, instance, owner):
      print('pobieranie...')
      return instance._name
   def __set__(self, instance, value):
      print('modyfikacja...')
      instance._name = value
   def __delete__(self, instance):
      print('usunięcie...')
      del instance._name

class Person2:                         # W Pythonie 2.6 należy użyć (object)
   def __init__(self, name):
      self._name = name
   name = Name()                      # Przypisanie deskryptora do atrybutu

bob = Person2('Robert Zielony')        # bob ma zarządzany atrybut
print(bob.name)                       # Wykonuje Name.__get__
bob.name = 'Robert A. Zielony'        # Wykonuje Name.__set__
print(bob.name)
del bob.name                          # Wykonuje Name.__delete__

anna = Person2('Anna Czerwona')        # anna także dziedziczy deskryptor
print(anna.name)
print(Name.__doc__)                   # Lub help(Name)