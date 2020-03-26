class Indexer:
    def __getitem__(self, index):
        return index ** 2

X = Indexer()
print(X[2])                                # X[i] wywołuje X.__getitem__(i)

for i in range(5):
    print(X[i], end=' ')


