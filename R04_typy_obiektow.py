import random
import math


###########
# liczby  #
###########
a = random.random()
print(a, math.pi)


####################
# lancuchy znakow  #
####################
s = "mielonka"
print(len(s), dir(s))
print(s[1], s[-1])
print(s[:3], s[3:5], s[:-5])
msg = """aaaa
bbbb"""
msg2 = "ccc\nddd"
msg3 = "eee" +\
       "fff"
print(msg, msg2, msg3)


############
# listy    #
############
L = [123, 'mielonka', 1.23]
L.append("NI")
print(L, L.pop(2))
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
col2 = [row[1] for row in M]
diag = [M[i][i] for i in [0, 1, 2]]
print(col2, diag)
G = (sum(rr) for rr in M)
print(G)
print(next(G))
print(next(G))


print("""
#############
# slowniki  #
#############""")
D = {x: ord(x) for x in "aaabbbccc"}
print(D)
D1 = {'aa': 11, 'bb': 22}
D2 = {}
D2['bb'] = 22
D2['cc'] = 33
D2['aa'] = 11
D3 = dict(aa=11, bb=22)
print(D1, D2, D3)

Ks = list(D2.keys())
Ks.sort()
print(Ks)
for k in Ks:
    print(k, '=>', D2[k])
for k in sorted(D2):
    print(k, '=>', D2[k])

x = 5
while x > 0:
    print('*' * x)
    x -= 1

if not 'cc' in D3:
    print("nie ma")
v1 = D3.get('cc', 0)
v2 = D3['cc'] if 'cc' in D3 else 1
print(v1, v2)


##########
#  sety  #
##########
S = {x for x in "aaabbbccc"}
print(S)
print(type(S))


###########
# krotki  #
###########
T = (1, 2, 3, 4)
print(T.index(4), T.count(4))
# T[0] = 2 # blad
print(T)


#########
# pliki #
#########
f = open('resources/data.txt', 'w')
f.write("Witaj\n")
f.write("tutaj\n")
f.close()
f = open('resources/data.txt')
text = f.read()
print(text)
print(dir(f), help(f.seek))
