def changer(a, b):                        # Do argumentów przypisano referencje do obiektów
    a = 2                                 # Zmiana wartości jedynie zmiennej lokalnej
    b[0] = 'mielonka'                     # Zmiana współdzielonego obiektu w miejscu

X = 1
L = [1, 2]                               # Wywołujący
changer(X, L)                            # Przekazanie obiektów niezmiennych i zmiennych

print(X, L)


def multiple(x, y):
    x = 2                                 # Modyfikacja jedynie zmiennych lokalnych
    y = [3, 4]
    return x, y                           # Zwrócenie nowych wartości w krotce

X = 1
L = [1, 2]
X, L = multiple(X, L)                    # Przypisanie wyników do zmiennych wywołującego
#X1, L1 = multiple(X, L)
print(X, L)
#print(X1, L1)

def f(a,b,c): print(a, b, c)
f(1,2,3)
f(c=9,b=44,a=0)

def f(a, b=22, c=33): print(a, b, c)
f(1,2,3)
f(1)
f(1,2)


def f(*args): print(args)
f(1)
f(1,2)
def f(**args): print(args)
f()
f(a=1,b=3,c=9)
def f(a, *pargs, **kargs): print(a, pargs, kargs)
f(1,2,3,b=9,u=8)

def func(a, b, c, d): print(a, b, c, d)
func(*(1, 2), **{'d': 4, 'c': 4})
T = (9,9,8,7)
func(*T)

def kwonly(a, *b, c):            # c - keyword-only argument
    print(a, b, c)

#kwonly(1,2,3) # blad
kwonly(1,2,c=3) # OK

def kwonly2(a, *, b, c):
    print(a, b, c)

#kwonly2(11, 22, 33) # blad
kwonly2(11, b=22, c=33) # OK