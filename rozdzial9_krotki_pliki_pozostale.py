x = (40)
y = (40,)
print(x, y)

T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)
tmp.sort()
T = tuple(tmp)
print(T)

T = ('cc', 'aa', 'dd', 'bb')
T = sorted(T)
print(T)

T = (1, 2, 3, 2, 4, 2)
print(T.index(3), T.index(2, 2), T.count(4))

T = (1, [2, 3], 4)
T[1][0] = 'cos'
print(T)

############################

p = open('data2.txt', 'w')
p.write("raz/n")
p.write("dwa/n")
p.close()
p = open('data2.txt')
print(p.readline())
print(p.readline())
print(p.readline())
print(p.readline())

print(open('data2.txt').read())

for line in open('data2.txt'):
    print(line)

data = open('data2.txt', 'rb').read()
print(data)

X, Y, Z = 43, 44, 45
S = 'Mielonka'
D = {'a': 1, 'b': 2}
L = [1, 2, 3]
F = open('data3.txt', 'w')
F.write(S + '\n')  # Zakończenie wierszy za pomocą \n
F.write('%s,%s,%s\n' % (X, Y, Z))  # Konwersja liczb na łańcuchy znaków
F.write(str(L) + '$' + str(D) + '\n')  # Konwersja i rozdzielenie znakiem $
F.close()

F = open('data3.txt')
print(F.readline())
print(F.readline())
line = F.readline()
print(line)

parts = line.split('$')  # Podział na znaku $
print(parts)

L = eval(parts[0])  # Konwersja na dowolny typ obiektu
print(L)

objects = [eval(P) for P in parts]  # To samo w jednej liście
print(objects)

D = {'a': 1, 'b': 2}
F = open('datafile.pkl', 'wb')
import pickle

pickle.dump(D, F)  # Serializacja dowolnego obiektu w pliku
F.close()
F = open('datafile.pkl', 'rb')
D2 = pickle.load(F)
print(D2)

F = open('data.bin', 'wb')  # Otwarcie pliku binarnego do zapisu
import struct

data = struct.pack('h', 8)  # Utworzenie spakowanych danych binarnych
print(data)
F.write(data)  # Zapisanie łańcucha bajtowego
F.close()
F = open('data.bin', 'rb')
data = F.read()
print(data)
values = struct.unpack('h', data)
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
L = ['a', X[:], 'b']
D = {'x': X[:], 'y': 2}
print(X, L, D)
X[1] = 'cos'
print(X, L, D)

s = ""
ss = "s"
if s:
    print('1')
if ss:
    print('2')
