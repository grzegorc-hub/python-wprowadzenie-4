# Super
# Definiuje funkcje method oraz delegate, które oczekują zmiennej action w klasach podrzędnych.
#
# Inheritor
# Nie udostępnia żadnych nowych zmiennych, dlatego wszystko ma zdefiniowane w klasie Super.
#
# Replacer
# Przesłania metodę method klasy Super za pomocą własnej wersji.
#
# Extender
# Dostosowuje metodę method klasy Super do własnych potrzeb, przesłaniając ją i wywołując w celu wykonania działania domyślnego.
#
# Provider
# Implementuje metodę action oczekiwaną przez metodę delegate klasy Super.

class Super:
   def method(self):
      print('w Super.method')                # Zachowanie domyślne
   def delegate(self):
      self.action()                          # Oczekuje zdefiniowania
   #def action(self):
      # assert False, 'musi byc!'
      #raise NotImplementedError('musi byc!!')

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

class Provider(Super):                       # Uzupełnienie wymaganej metody
   def action(self):
      print('w Provider.action')


if __name__ == '__main__':

   for klass in (Inheritor, Replacer, Extender):
      print('\n' + klass.__name__ + '...')
      klass().method()

   print('\nProvider...')
   x = Provider()
   x.delegate()

   # X = Super()
   # X.delegate()
