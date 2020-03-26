from rozdzial27 import Person

bob = Person('Robert Kowal')
print(bob)
print(bob.__class__)

print( bob.__class__.__name__ )

print( list(bob.__dict__.keys()) ) # Atrybuty są tak naprawdę kluczami słownika

for key in bob.__dict__:
    print(key, '=>', bob.__dict__[key]) # Ręczne indeksowanie

for key in bob.__dict__:
    print(key, '=>', getattr(bob, key))


from rozdzial27 import Person, Manager # Załadowanie naszych klas
bob = Person('Robert Zielony') # Ponowne utworzenie obiektów do przechowania
anna = Person('Anna Czerwona', job='programista', pay=100000)
tom = Manager('Tomasz Czarny', 50000)
import shelve
db = shelve.open('persondb') # Nazwa pliku, w którym przechowywane są obiekty
for object in (bob, anna, tom): # Użycie atrybutu name obiektu jako klucza
 db[object.name] = object # Przechowanie obiektu w pliku shelve po kluczu
db.close() # Zamknięcie po wprowadzeniu zmian