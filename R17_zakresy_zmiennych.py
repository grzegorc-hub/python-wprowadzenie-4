# Zakres globalny
X = 99                                       # X i func przypisane w module: globalne
def func(Y):                                 # Y i Z przypisane w funkcji: lokalne
   # Zakres lokalny
   Z = X + Y                                 # X jest globalne
   return Z

print( func(1) )                             # func w module: wynik = 100

import builtins
print(dir(builtins))

def hider():
    open = 'cos'
    f = open('resources/data3.txt')

#hider()

def func2():
    X = 22
    print(X)

func2()
print(X)

print(10*'*')

X = 88                                       # Zmienna globalna X
def func():
   X = 99                                    # Zmienna lokalna X: ukrywa globalną
func()
print(X)                                     # Wyświetla 88: bez zmian


X = 88                                       # Zmienna globalna X
def func():
   global X
   X = 99                                    # Zmienna globalna X: poza def
func()
print(X)                                     # Wyświetla 99

y, z = 1, 2                                  # Zmienne globalne w module
def all_global():
   global x                                  # Deklaracja przypisanych zmiennych globalnych
   x = y + z                                 # Nie trzeba przypisywać y i z — działa reguła LEGB


X = 99                                       # Zmienna z zakresu globalnego — nieużywana
def f1():
   X = 88                                    # Zmienna lokalna z zakresu zawierającego
   def f2():
      print(X)                               # Referencja w zagnieżdżonej instrukcji def
   f2()
f1()                                         # Wyświetla 88 — zmienną lokalną funkcji zawierającej


def maker(N):                                # (funkcja fabryczna)
    def action(X):                           # Utworzenie i zwrócenie funkcji action
        return X ** N                        # Funkcja action zachowuje N z zakresu funkcji zawierającej
    return action

f = maker(2)
print( f(3) )
print( f(4) )

def tester(start):
   state = start                             # Każde wywołanie otrzymuje własną zmienną state
   def nested(label):
      nonlocal state                         # Pamięta state z zakresu funkcji zawierającej
      print(label, state)
      state += 1                             # Można zmienić, jeśli nonlocal
   return nested

F = tester(0)
F('mielonka')
F('cos')
F('cos2')


#################################


x = 0
def outer():
    x = 1
    def inner():
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)


x = 0
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)


x = 0
def outer():
    x = 1
    def inner():
        global x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

#########################################

print("globals: ", globals())
print("locals: ", locals())
print("vars: ", vars())

def foo():
    a = 11
    print("globals: ", globals())
    print("locals: ", locals())
    print("vars: ", vars())

foo()




