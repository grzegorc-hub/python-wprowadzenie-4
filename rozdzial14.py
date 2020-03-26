f = open('data3.txt')
print(f.__next__())
print(f.__next__())

for l in open('data3.txt'):
    print(l, end='')

L = [1, 2, 3]
I = iter(L)
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
print(D.keys())

L = [x + 1 for x in L]
print(L)

L = [line.upper() for line in open('data3.txt')]
print(L)

L = [line.upper() for line in open('data3.txt') if line[0] == 'M']
print(L)

L = ['aaa', 'bbb']
LL = list(map(str.upper, L))
print(LL)
