from abc import ABCMeta, abstractmethod

# abstrakcyjna klasa nadrzędna

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

   print('\nProvider...')
   x = Provider()
   x.delegate()

   #X = Super() # Can't instantiate abstract class Super with abstract methods action

   class Sub(Super): pass
   #X = Sub() # Can't instantiate abstract class Sub with abstract methods action

   class Sub(Super):
      def action(self): print('mielonka')

   X = Sub()
   X.delegate()
