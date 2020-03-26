import random
import math

a = random.random()
print(a, math.pi)

s= "mielonka"
print(len(s),dir(s))
print(s[1],s[-1])
print(s[:3],s[3:5],s[:-5])

msg = """aaaa
bbbb"""
msg2 = "ccc\nddd"
print(msg, msg2)

L = [123, 'mielonka', 1.23]
L.append("NI")
print(L, L.pop(2))

M = [[1,2,3],
     [4,5,6],
     [7,8,9]]
col2 = [row[1] for row in M]
diag = [M[i][i] for i in [0,1,2]]
print(col2, diag)

G = (sum(rr) for rr in M)
print(next(G))
print(next(G))

S = {x for x in "aaabbbccc"}
D = {x: ord(x) for x in "aaabbbccc"}
print(S,D)

D1 = {'aa':11,'bb':22}
D2 = {}
D2['aa'] = 11
D2['bb'] = 22
D3 = dict(aa=11,bb=22)
print(D1, D2, D3)

Ks = list(D1.keys())
Ks.sort()
print(Ks)
for k in Ks:
     print(k, '=>', D1[k])
for k in sorted(D1):
     print(k, '=>', D1[k])

x = 5
while x > 0:
     print('*' * x)
     x -= 1

if not 'cc' in D3:
     print("nie ma")

v1 = D2.get('cc', 0)
v2 = D2['cc'] if 'cc' in D2 else 1
print(v1, v2)

T = (1,2,3,4)
print(T.index(4), T.count(4))
#T[0] = 2
print(T)

f = open('data.txt', 'w')
f.write("Witaj\n")
f.write("tutaj\n")
f.close()

f = open('data.txt')
text = f.read()
print(text)
print(dir(f), help(f.seek))