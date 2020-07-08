import R22_moduly2a
R22_moduly2a.printer("joerjf")

from R22_moduly2a import printer
printer("iieji")

from R22_moduly2b import spam
print(spam)

from R22_moduly2a import *
printer("dsfsdf")

print(R22_moduly2a.spam)
R22_moduly2a.spam = 2
import R22_moduly2a
print(R22_moduly2a.spam)

Y[0] = 'jief'
print(Y)

print(R22_moduly2a.__dict__.keys())

from imp import reload
reload(R22_moduly2a)