def mysum(L):
    print(L)                               # Śledzenie poziomów rekurencji
    if not L:                              # L z każdym wywołaniem ma coraz mniejszą długość
        return 0
    else:
        return L[0] + mysum(L[1:])

mysum([1, 2, 3, 4, 5])

def echo(msg):
    print(msg)

x = echo
x("jhioerhjgio")

schedule = [(echo, "aaa"), (echo, "bbb")]
for x,y in schedule:
    x(y)

print(echo.__name__)
print(echo.__code__.co_varnames)

def func(a, b, c):
    return a + b + c

def func(a: 'mielonka', b: (1, 10), c: float) -> int:
    return a + b + c

print(func.__annotations__)

f = lambda x,y,z: x + y + z
print( f(1,2,3) )

L = [(lambda x: x**2),                #Wewnętrzna definicja funkcji
    (lambda x: x**3),
    (lambda x: x**4)]                 #Lista trzech wywoływanych funkcji
for f in L:
    print(f(2))

c = [1,2,3,4,5]
def inc(x): return x+10
m = map(inc,c)
print(list(m))
m2 = map(lambda x:x+20, c)
print(list(m2))
m3 = map(lambda x,y: x*y, c,c)
print(list(m3))


f = filter((lambda x: x > 0), range(-5, 5))
print(list(f))
from functools import reduce
r = reduce((lambda x, y: x + y), [1, 2, 3, 4])
print(r)