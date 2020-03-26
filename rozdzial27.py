class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):  # Dodana metoda
        return '[Person: %s, %s]' % (self.name, self.pay)

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, "manager", pay)
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent+bonus)

class Manager2:
    def __init__(self, name, pay):
        self.person = Person(name, 'manager', pay) # Osadzenie obiektu Person
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus) # Przechwycenie i delegowanie
    def __getattr__(self, attr):
        return getattr(self.person, attr) # Delegowanie wszystkich pozostałych atrybutów
    def __str__(self):
        return str(self.person) # Musi znowu przeciążać operator (w 3.0)

if __name__ == '__main__':
    bob = Person('Robert Zielony')  # Test klasy
    anna = Person('Anna Czerwona', job='programista', pay=100000)  # Automatycznie wykonuje __init__
    print(bob)  # Pobranie dołączonych atrybutów
    print(anna)

    print(bob.lastName(), anna.lastName())  # Użycie nowych metod
    anna.giveRaise(.10)  # zamiast kodu zapisanego na stałe
    print(anna)

    tom = Manager('Tomasz Czarny', 50000)  # Utworzenie obiektu Manager: __init__
    tom.giveRaise(.10)  # Wykonanie własnej wersji
    print(tom.lastName())  # Wykonanie odziedziczonej metody
    print(tom)  # Wykonanie odziedziczonej __str__

    for o in (anna, bob, tom):
        o.giveRaise(.5)
        print(o)

    dylan = Manager2("Dylan B", 1000)
    print(dylan)
    print(dylan.name)
