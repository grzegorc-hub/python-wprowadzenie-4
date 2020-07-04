x = (40)
y = (40,)
z = 40,
print(x, y, z)
print(type(x), type(y), type(z))

T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)
tmp.sort()
T = tuple(tmp)
print(T)

T = ('cc', 'aa', 'dd', 'bb')
T = sorted(T)
print(T)

T = (1, 2, 3, 2, 4, 2)
print(T.index(2), # Przesunięcie pierwszego wystąpienia obiektu 2
      T.index(2, 2), # Przesunięcie wystąpienia po przesunięciu 2
      T.count(4))

T = (1, [2, 3], 4)
print(T, T[0])
#T[0] = 11 # blad
T[1][0] = 'cos'
print(T)

############################

p = open('resources/data2.txt', 'w')
p.write("raz\n")
p.write("dwa\n")
p.close()
p = open('resources/data2.txt')
print(p.readline())
print(p.readline())
print(p.readline())
print(p.readline())

print(open('resources/data2.txt').read())

for line in open('resources/data2.txt'):
    print(line)

data = open('resources/data2.txt', 'rb').read()
print(data)

X, Y, Z = 43, 44, 45
S = 'Mielonka'
D = {'a': 1, 'b': 2}
L = [1, 2, 3]
F = open('resources/data3.txt', 'w')
F.write(S + '\n')  # Zakończenie wierszy za pomocą \n
F.write('%s,%s,%s\n' % (X, Y, Z))  # Konwersja liczb na łańcuchy znaków
F.write(str(L) + '$' + str(D) + '\n')  # Konwersja i rozdzielenie znakiem $
F.close()

F = open('resources/data3.txt')
print(F.readline())
print(F.readline())
line = F.readline()
print(line)

parts = line.split('$')  # Podział na znaku $
print(parts)

L = eval(parts[0])  # Konwersja na dowolny typ obiektu (eval traktuje łańcuch znaków jako fragment kodu wykonywalnego)
print(L)

objects = [eval(P) for P in parts]  # To samo w jednej liście
print(objects)

D = {'a': 1, 'b': 2}
F = open('resources/datafile.pkl', 'wb')
import pickle
pickle.dump(D, F)  # Serializacja dowolnego obiektu w pliku
F.close()
F = open('resources/datafile.pkl', 'rb')
D2 = pickle.load(F)
print("pickle test")
print(D2)

F = open('resources/data.bin', 'wb')  # Otwarcie pliku binarnego do zapisu
import struct
data = struct.pack('ih', 7, 8)  # Utworzenie spakowanych danych binarnych
print("struct test")
print(data)
F.write(data)  # Zapisanie łańcucha bajtowego
F.close()
F = open('resources/data.bin', 'rb')
data = F.read()
print(data)
values = struct.unpack('ih', data)
print(values)

with open(r'C:\Users\Maciek\PycharmProjects\python_wprowadzenie\data3.txt') as myfile:
    for line in myfile:
        print(line)

#################

X = [1, 2, 3]
L = ['a', X, 'b']
D = {'x': X, 'y': 2}
print(X, L, D)
X[1] = 'cos'
print(X, L, D)

X = [1, 2, 3]
L = ['a', X.copy(), 'b']
D = {'x': X[:], 'y': 2}
print(X, L, D)
X[1] = 'cos'
print(X, L, D)

s = ""
ss = "s"
L = []
LL = [1]
a = 0
if s:
    print('1')
if ss:
    print('2')
if L:
    print('3')
if LL:
    print('4')
if a:
    print('5')
if None:
    print('6')

print(bool('mniam'))
print(bool(L))
