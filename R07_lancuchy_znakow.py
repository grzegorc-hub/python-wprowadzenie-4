import sys

print('ryce"rz', "ryce'rz")
print('ryce\'rz', "ryce\"rz")
title = "Zywot" "Briana"
print(title)

s = 'a\nb\tc'
print(len(s), s)
s = 'a\0b\001c\x02d'
print(len(s), s)

s1 = 'C:\nowy\tekst.dat'
s2 = r'C:\nowy\tekst.dat' # raw string
print(s1, s2)

s = "abc" + "edf"
print(s, '\t', 10*'-')

job = 'haker'
for c in job: print(c, end=' ')
print("k" in job, "er" in job, 'hh' in job)

S = 'mielonka'
print(S[0], S[-2])
print(S[1:3], S[1:], S[:-1])

S = 'abcdefghijklmnop'
print( S[1:10:2], S[::2] )
print( S[::-1], S[4:0:-1] )

help('repr')
S1 = 42 + int("1")
S2 = "42" + str(1)
S3 = repr(42)
S4 = repr('cos')
# S5 = "2" + 45 # BŁĄD
print(S1, S2, S3, S4)

help('ord')
help('chr')
print(ord('s'), chr(115))

i = int('1111', 2)
print(i, )
print("i=", i)
b = bin(14)
print(b)
print(type(i), type(b))
h = '0xff'
print(int(h,16))

S = 'a-b-c-d'
f = S.find('b')
S1 = S.replace('-', '')
S2 = S.replace('-', '', 1)
print(f, S1, S2)

S = 'brama'
L = list(S)
print(L)
L[2] = 'e'
L[3] = 'j'
S = ''.join(L)
print(S)
#S[0] = 'B' # blad!

S = 'aaa,bbb ccc'
cols = S.split(',')
print(cols)

line = "iojeif iejfjeii    "
print(line.rstrip(), line.upper(), line.isalpha(), line.startswith('io'))

#######################

S1 = 'Ten %d %s jest martwy %.2f' % (1,'ptak', 1/3)
print(S1)

reply = """
Witamy...
Witaj %(name)s!
Twój wiek to %(age)s lat.
"""
values = {'name': 'Amadeusz', 'age': 40}
S = reply % values
print(S)
print(vars())

S2 = 'Ten {0} {1} jest martwy {cos:.4f} i {2.platform}'.format(1, 'ptak', sys, cos=1/3)
print(S2)

name = "Eric"
name2 = "Bob"
profession = "Comedian"
age = 74
s = f"Hello, {name}. You are {age}. Me is {age-40}. Look at {name2.upper()}"
print(s)

message1 = (
    f"Hi {name}. "
    f"You are a {profession}. "
)
message2 = f"Hi {name}. " \
           f"You are a {profession}. "
print(message1)
print(message2)
