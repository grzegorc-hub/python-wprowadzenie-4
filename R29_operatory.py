class Indexer:
    def __getitem__(self, index):
        return index ** 2

X = Indexer()
print(X[2])                                # X[i] wywołuje X.__getitem__(i)

for i in range(5):
    print(X[i], end=' ')


class Squares:
    '''
    klasa ktora implementuje protokól iteracji
    '''
    def __init__(self, start, stop):          # Zapisanie stanu przy utworzeniu
        self.value = start - 1
        self.stop = stop
    def __iter__(self):                       # Otrzymanie obiektu iteratora na iter()
        return self
    def __next__(self):
        if self.value == self.stop:           # Również wywoływane przez funkcję wbudowaną next
            raise StopIteration
        self.value += 1
        return self.value ** 3


for i in Squares(1, 5):                        # for wywołuje metodę iter(), która wywołuje __iter__()
    print(i, end='-')                          # Każda iteracja wywołuje metodę next()

print()

class Iters:
    def __init__(self, value):
        self.data = value
    def __getitem__(self, i):               # Metoda zastępcza do użycia przez iterację
        print('get[%s]:' % i, end='')       # oraz do indeksowania i wycinania
        return self.data[i]
    def __iter__(self):                     # Metoda preferowana w iteracji
        print('iter=> ', end='')            # Pozwala na użycie tylko jednego iteratora
        self.ix = 0
        return self
    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item
    def __contains__(self, x):              # Metoda preferowana w operacji 'in'
        print('contains: ', end='')
        return x in self.data

X = Iters([1, 2, 3, 4, 5])                  # Utworzenie instancji
print(3 in X)                               # Przynależność
for i in X:                                 # Pętle for
    print(i, end=' | ')
print()
print([i ** 2 for i in X])                  # Inne konteksty iteracyjne
print(list(map(bin, X)))

I = iter(X)                                 # Ręczna iteracja (demonstracja mechanizmu stosowanego
                                            # w kontekstach iteracyjnych)
while True:
    try:
        print(next(I), end=' @ ')
    except StopIteration:
        break


class empty:
    def __getattr__(self, attrname):
        if attrname == "age":
            return 40
        else:
            raise AttributeError(attrname)

X = empty()
print()
print(X.age)
#print(X.name) #blad


class Callee:
    def __call__(self, *pargs, **kargs):         # Przechwytuje wywołania instancji
        print('Wywołanie:', pargs, kargs)        # Akceptuje dowolne argumenty
...
C = Callee()
C(1, 2, 3)                                       # C jest obiektem wywoływanym
C(1, 2, 3, x=4, y=5)