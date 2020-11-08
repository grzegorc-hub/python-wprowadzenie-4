import R22_moduly2a
R22_moduly2a.printer("foo")

from R22_moduly2a import printer
printer("boo")

from R22_moduly2b import *
print(spam)
print(spam2)
#print(spam3)

from R22_moduly2a import *
printer("cow")

print(R22_moduly2a.spam)
R22_moduly2a.spam = 2
import R22_moduly2a
print(R22_moduly2a.spam)

Y[0] = 'yet'
print(Y)

print(R22_moduly2a.__dict__.keys())

from imp import reload
reload(R22_moduly2a)