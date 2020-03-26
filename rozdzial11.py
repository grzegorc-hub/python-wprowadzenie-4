(a, b, c) = "ABC"
print(a)

s = 'jajo'
a,b,c,d = s
print(c)

L = [1,2,3,4]
while L:
    front, L = L[0], L[1:]
    print(front, L)

seq = (1,2,3,4)
a, *b = seq
print(a, b)

ss = 'mielonks'
a, b, *c = ss
print(a,b,c)

L = [1,2,3,4]
while L:
    front, *L = L
    print(front, L)

a = b = c = 'mielonka'
print(a,b,c)

x = 1
x += 1
print(x)

L = [1,2,3,4]
L += [5,6]
print(L)

x = 'mielonka'
y = 99
z = ['jajka']
print(x, y, z, sep='...', end='!\n')
print(x, y, z, sep='...', file=open('data11.txt', 'w'))

import sys
sys.stdout.write("ioejoifjei")

sys.stdout = open('log.txt', 'a')
print(x,y,z)

log = open('log2.txt', 'w')
print(1, 2, 3, file=log)