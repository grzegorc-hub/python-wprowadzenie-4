
from R39_metaklasy_library import Base

class Derived(Base):
    def bar(self):
        return 'bar'


I = Derived()
print(I.foo())