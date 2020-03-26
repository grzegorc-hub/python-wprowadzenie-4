print(len([1, 2, 3]))
S1 = [1, 2, 3] + [4, 5, 6]
S2 = ['Ni!'] * 4
print(S1, S2)

N = [5,6]
S3 = str([1, 2]) + "34"
S4 = [1, 2] + list("34")
S5 = str(N) + "999"
print(S3, S4, S5)

print(3 in [1, 2, 3])
L = list(map(abs, [-1, -2, 0, 1, 2]))
print(L)

L = ['mielonka', 'Mielonka', 'MIELONKA!']
L[1] = 'jajka' # Przypisanie do indeksu
print(L)
L[0:2] = ['najsmaczniejsza', 'jest'] # Przypisanie do wycinka: usunięcie i wstawienie
print(L)

L.append('sortowana')
L.sort()
print(L)
L.sort(key=len)
print(L)
print(L[::-1])

L = ['abc', 'ABD', 'aBe']
L = sorted(L, key=str.lower, reverse=True)
print(L)

L = [1,2]
L.extend([3,4,1])
print(L)
L.pop()
print(L.pop())
print(L)

L.reverse()
LL = list(reversed(L))
print(L, LL)

L = ['mielonka', 'jajka', 'szynka']
print(L.index('jajka'))
L.insert(1, 'tost')
print(L)
L.pop(0)
L.remove('jajka')
print(L)
L.insert(1, 'tosty')
L.insert(1, 'toster')
L.insert(1, 'tostery')
print(L)
del L[0]
print(L)
del L[1:]
print(L)

L = ['Mam', 'już', 'coś']
L[1:] = []
print(L)
L[0] = []
print(L)

##########################################

D = {'mielonka': 2, 'szynka': 1, 'jajka': 3}
print(D['mielonka'])
print(D)
print('szynka' in D)
print(type(D.keys()))
print(list(D.keys()))

D['szynka'] = ['grillowanie', 'pieczenie', 'smażenie']
del D['jajka']
D['lunch'] = 'Bekon'
print(D)
print(list(D.values()))
print(D.items())

print(D.get('lunch'))
print(D.get('tost'))
print(D.get('tost', 88))

D1 = {'jajka': 3, 'szynka': 1, 'mielonka': 2}
D2 = {'tost':4, 'ciastko':5}
D1.update(D2)
#D3 = D1 + D2 not working
print(D1)
D1.pop('tost')
print(D1)

L = []
#L[99] = 'mielonka'
D = {}
D[99] = 'mielonka'
print(D[99])

Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99

if ((2,3,6) in Matrix):
    print(Matrix[(2,3,6)])
else:
    print(0)

try:
    print(Matrix[(2, 3, 6)])
except KeyError:
    print(0)

print(Matrix.get((2,3,4), 0))
print(Matrix.get((2,3,6), 0))

mel = {'name': "mark",
       'home': {'state': "pl", 'zip': "000"}}
print(mel['home']['zip'])

D1 = dict([('name', 'mel'), ('age', 45)])
D2 = dict.fromkeys(['a', 'b'], 0)
print(D1, D2)

D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(D)
D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)
D = {x: x ** 2 for x in [1, 2, 3, 4]}
print(D)
D = {k: ord(k) for k in ' mielonka '}
print(D)

print(D.keys(), D.values(), D.items())
print(list(D.keys()), list(D.values()))

for k in sorted(D):
    print(k, D[k])