X = 0

if X:
    def func1():
        print("1")
else:
    def func1():
        print('2')

func1()
test = func1
test()
test.aa = 3
test()
print(test.aa)

def times(x, y):
    return x * y

x = times(2,8)
y = times(2,'nie')
print(x, y)

def intersect(seq1, seq2):
   res = []                                  # Na początek pusta lista
   for x in seq1:                            # Przeszukanie pierwszej sekwencji
      if x in seq2:                          # Powtarzający się element?
         res.append(x)                       # Dodanie na końcu listy wyników
   return res

s1 = 'mielonka'
s2 = 'malolata'
s3 = intersect(s1, s2)
print(s3)

x = intersect([1, 2, 3], (1, 4))
print(x)

# print(res)
# y = intersect(1,2) # blad