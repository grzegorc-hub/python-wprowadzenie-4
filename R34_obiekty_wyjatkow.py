class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

def raiser0():
   X = General()                             # Zgłoszenie instancji klasy nadrzędnej
   raise X
def raiser1():
   X = Specific1()                           # Zgłoszenie instancji klasy podrzędnej
   raise X
def raiser2():
   X = Specific2()                           # Zgłoszenie instancji innej klasy podrzędnej
   raise X

#for func in (raiser0, raiser1, raiser2):
for func in (raiser1, raiser2):
   try:
      func()
   #except General:                           # Dopasowanie General lub którejś z jej podklas. Lepsze niz lista wyjatkow, bo mozna zpomniec o jakis, lub gdy dochodzi nowy to trzeba pamietac aby go dodac
   except(Specific1, Specific2):
      import sys
      print('przechwycono:', sys.exc_info()[0])

#######################

# BaseException
# Exception
# ArithmeticError
# OverflowError

#######################

class MyBad(Exception):
    def __str__(self):
        return 'Zawsze patrz na życie z humorem...'

try:
    raise MyBad()
except MyBad as X:
    print(X)


#######################

class FormatError(Exception):
   logfile = 'resources/formaterror.txt'
   def __init__(self, line, file):
      self.line = line
      self.file = file
   def logerror(self):
      log = open(self.logfile, 'a')
      print('Błąd w', self.file, self.line, file=log)

def parser():
   raise FormatError(40, 'spam.txt')

try:
   parser()
except FormatError as exc:
   exc.logerror()
