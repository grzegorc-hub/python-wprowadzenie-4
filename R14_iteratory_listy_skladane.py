f = open('resources/data3.txt')
print(f.__next__())
print(f.__next__())
print(next(f))

for l in open('resources/data3.txt'):
    print(l, end='')

L = [1, 2, 3]
I = iter(L) # pozyskanie obiektu iteratora
print(next(I))
print(next(I))

for i in L:
    print(i ** 2, end='')

I = iter(L)
while True:
    try:
        i = next(I)
        print(i ** 2, end='')
    except StopIteration:
        break;

D = {}
print(D.keys()) # nie lista, a obiekt widoku (widoki nie sa iteratorami)
print(type(D.keys()))

DD = {1: 'a', 2: 'b'}
#print(next(DD)) # blad
print(next(iter(DD)))
print(next(iter(DD.keys())))
view_on_keys = DD.keys()
print(dir(view_on_keys))
# The objects returned by dict.keys(), dict.values() and dict.items() are view objects
# They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes.
# Dictionary views can be iterated over to yield their respective data, and support membership tests.

##########################################

L = [x + 1 for x in L]
print(L)

L = [line.upper() for line in open('resources/data3.txt')]
print(L)

L = [line.upper() for line in open('resources/data3.txt') if line[0] == 'M']
print(L)

L = ['aaa', 'bbb']
LL = list(map(str.upper, L))
print(LL)
