
assert 2==2

######################

try:
    with open('resources/data3aa.txt') as myfile:
        for line in myfile:
            print(line)
except Exception as X:
    print("blad" + str(X.args))
else:
    print('bez bledu')
finally:
    print('koniec')


#######################

import sys

def action2():
   print(1 + [])                                  # Wygenerowanie wyjątku TypeError

def action1():
   try:
        action2()
   except TypeError as e:                         # Najbardziej aktualna pasująca instrukcja try
        print(sys.exc_info())
        print('wewnętrzne try')
        #print(e)
        #raise e

try:
   action1()
except TypeError:                                  # Tutaj tylko jeśli action1 ponownie zgłasza wyjątek
   print('zewnętrzne try')

print(sys.exc_info())


###########################

class Bad(Exception):                              # Wyjątek zdefiniowany przez użytkownika
    pass

def doomed():
    raise Bad()

try:
    doomed()
except Bad:
    print('przechwycenie Bad')


def test01():
    try:
        doomed()
    except Bad:
        print("except called")
        return 1
    finally:
        print("finally called")
        return 2

a = test01()
print(a)