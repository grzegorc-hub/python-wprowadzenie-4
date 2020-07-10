class AttrDisplay:
    """
    Udostępnia dziedziczoną metodę przeciążania wyświetlania, która pokazuje instancje z ich nazwami klas, a także parę
    nazwa=wartość dla każdego atrybutu przechowanego w samej instancji (ale nie atrybutów odziedziczonych po klasach).
    Można ją wmieszać w dowolną klasę i będzie działała na dowolnej instancji.
    """
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))  # getattr(x, 'y') is equivalent to x.y
        return ', '.join(attrs)
    def __str__(self):
        return 'Printing [%s: %s]' % (self.__class__.__name__, self.gatherAttrs())

#class Person():                                           # pierwsza wersja
class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    #def __str__(self):  # Dodana metoda
    #    return '[Person: %s, %s]' % (self.name, self.pay)

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, "manager", pay)
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent+bonus)

class Manager2:                                             # Przyklad wzorca delegacja (dziedzicznie lepsze raczej)
    def __init__(self, name, pay):
        self.person = Person(name, 'manager', pay)          # Osadzenie obiektu Person (wzorzec 'composite')
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)              # Przechwycenie i delegowanie
    def __getattr__(self, attr):
        return getattr(self.person, attr)                   # Delegowanie wszystkich pozostałych atrybutów
    def __str__(self):
        return str(self.person)                             # Musi znowu przeciążać operator (w 3.0)

class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, member):
        self.members.append(member)
    def giveRise(self, percent):
        for p in self.members:
            p.giveRaise(percent)
    def showAll(self):
        for p in self.members:
            print(p)

if __name__ == '__main__':
    bob = Person('Robert Zielony')
    anna = Person('Anna Czerwona', job='programista', pay=100000)
    print(bob)
    print(anna)

    print(bob.lastName(), anna.lastName())
    anna.giveRaise(.10)
    print(anna)

    tom = Manager('Tomasz Czarny', 50000)
    tom.giveRaise(.10)                                      # Wykonanie własnej wersji
    print(tom.lastName())                                   # Wykonanie odziedziczonej metody
    print(tom)                                              # Wykonanie odziedziczonej __str__

    for o in (anna, bob, tom):
        o.giveRaise(.5)
        print(o)

    dylan = Manager2("Dylan B", 1000)
    print(dylan)
    print(dylan.name)

    dd = Department(bob, anna)
    dd.addMember(tom)
    dd.addMember(dylan)
    dd.giveRise(.01)
    dd.showAll()

    print(tom.__class__)
    print(tom.__dict__)
    print(Manager.__name__)
    print(Manager.__bases__)