
from R39_metaklasy_library import Base

class Derived(Base):
    def bar(self):
        return 'bar'


I = Derived()
print(I.foo())


class Derived2(Base):
    ...


I2 = Derived2()
print(I2.foo())
