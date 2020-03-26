import module1
module1.printer("joerjf")

from module1 import printer
printer("iieji")

from module1 import *
printer("dsfsdf")

print(module1.spam)
module1.spam = 2
import module1
print(module1.spam)

Y[0] = 'jief'
print(Y)

print(module1.__dict__.keys())

from imp import reload
reload(module1)