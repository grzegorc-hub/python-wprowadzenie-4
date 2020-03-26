y = 253

x = y // 2                                   # Dla jakiegoś y > 1
while x > 1:
   if y % x == 0:                            # Reszta
      print(y, 'ma czynnik', x)
      break                                  # Pominięcie reszty
   x -= 1
else:                                        # Normalne wyjście
   print(y, 'jest liczbą pierwszą')


# for <cel> in <obiekt>:                       # Przypisanie elementów obiektu do celu
# #    <instrukcje>                              # Powtarzane ciało pętli: użycie celu
# # else:
# #    <instrukcje>                              # Jeśli nie trafiliśmy na break

T = [(1, 2), (3, 4), (5, 6)]
for both in T:
    a, b = both                             # Odpowiednik z przypisaniem ręcznym
    print(a, b)

print(range(5))
print(list(range(5)))

for i in range(3):
    print(i, end='-')

S = 'abcdefghijk'
for c in S[::2]: print(c, end=' ')

L = [1,2,3,4,5]
for i in range(len(L)):
    L[i] += 1

print(L)

L1 = [1,2,3]
L2 = [7,8,9]
for (x, y) in zip(L1, L2):
    print(x, y, '--', x+y)

L = list(map(ord, 'mielonka'))
print(L)

S = 'mielonka'
E = enumerate(S)
print( next(E) )
print( next(E) )

for i,v in enumerate(S):
    print(i, v)