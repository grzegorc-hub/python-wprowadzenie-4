'''
Map VS List Comprehension. List comprehension is more concise and easier to read as compared to map.
List comprehension are used when a list of results is required as map only returns a map object and
does not return any list. Map is faster in case of calling an already defined function (as no lambda is required).
'''

L = [x for x in range(5) if x % 2 == 0]
f = filter((lambda x: x % 2 == 0), range(5))
print(L, list(f))

print(range(5))

res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
print(res)

#################################

def gensquares(N):
    for i in range(N):
        yield i ** 2

print(type(gensquares(4)))

g = gensquares(4)
print(type(g))

print( next(g) )
print( next(g) )
print( next(g) )

for i in gensquares(10):
    print(i, end=' :')

g = (x ** 2 for x in range(4))          # Wyrażenie generatora
print(g)
print(list(g))
g = (x ** 2 for x in range(4))
print(next((g)))
print(next((g)))

s = {x * x for x in range(10)}          # Zbiór składany
print(s)
d = {x: x * x for x in range(10)}       # Słownik składany, nowość w 3.0
print(d)

###################################

X = 99
def selector0():
    print(X)
selector0()

X = 99
def selector1():
    print(X)                # python kompilując kod funkcji, napotyka przypisanie do nazwy X, więc decyduje, że jest to zmienna lokalna funkcji. Jednak na etapie wykonania funkcja print jest wywoływana przed przypisaniem, przez co zmienna lokalna X nie jest jeszcze zdefiniowana
    X = 88
# selector1()               # BLAD! UnboundLocalError: local variable 'X' referenced before assignment

X = 99
def selector2():
    import __main__         # Zaimportowanie własnego modułu
    print(__main__.X)       # Kwalifikowane odwołanie w celu uzyskania globalnej wersji nazwy
    X = 88                  # Niekwalifikowane odwołanie użyje wersji lokalnej
    print(X)                # Wypisanie lokalnej wersji
selector2()


# Domyślne wartości argumentów są wyliczane i zapisywane statycznie podczas wywołania instrukcji def,
# nie przy wywołaniu samej funkcji.
def saver(x=[]):               # Zapisuje pustą listę (obiekt mutowalny) jako wartosc domyslna
    x.append(1)                # Powoduje modyfikację wartości domyślnej!
    print(x)

saver([2])                     # Wartość domyślna nie jest użyta
saver()                        # Wartość domyślna jest użyta
saver()                        # Rośnie przy każdym wywołaniu!
saver()


def saver():
    saver.x.append(1)
    print(saver.x)

saver.x = []
saver()
saver()
saver()
