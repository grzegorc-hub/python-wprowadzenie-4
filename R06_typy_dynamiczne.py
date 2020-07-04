x = 42
x = 'zywoplot'
x = 3.14
x = [1, 2, 3]
print(x)

a = 3
b = a
a = 'mielonka'
print(a, b)

L1 = [23, 24, 25]
L2 = L1
L3 = L1[:]
L1[1] = 44
print(L1, L2, L3)

L = [1, 2, 3]
M = L
K = [1, 2, 3]
print(L == M, L is M)
print(L == K, L is K)

x = 42
y = 42
print(x == y, x is y)  # cache!

import sys # PEP 8
print(sys.getrefcount(x))
print(sys.getrefcount(y))
print(sys.getrefcount(1))
print(sys.getrefcount(L))