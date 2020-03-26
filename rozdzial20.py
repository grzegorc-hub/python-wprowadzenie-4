L = [x for x in range(5) if x % 2 == 0]
f = filter((lambda x: x % 2 == 0), range(5))
print(L, list(f))

print(range(5))

res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
print(res)

def gensquares(N):
    for i in range(N):
        yield i ** 2

g = gensquares(4)
print( next(g) )
print( next(g) )
print( next(g) )

for i in gensquares(10):
    print(i, end=' :')

g = (x ** 2 for x in range(4))
print(g)
print(list(g))

g = (x ** 2 for x in range(4))
print(next((g)))
print(next((g)))

s = {x * x for x in range(10)}                # Zbiór składany
print(s)
d = {x: x * x for x in range(10)}     # Słownik składany, nowość w 3.0
print(d)

X = 99
def selector():
    import __main__         # Zaimportowanie własnego modułu
    print(__main__.X)       # Kwalifikowane odwołanie w celu uzyskania globalnej wersji nazwy
    X = 88                  # Niekwalifikowane odwołanie użyje wersji lokalnej
    print(X)                # Wypisanie lokalnej wersji

selector()

def saver():
    saver.x.append(1)
    print(saver.x)

saver.x = []
saver()
saver()
