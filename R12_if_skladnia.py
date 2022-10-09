choice = 'szynka'

if choice == 'mielonka':
    print(1.25)
elif choice == 'szynka':
    print(1.99)
elif choice == 'jajka':
    print(0.99)
elif choice == 'boczek':
    print(1.10)
else:
    print('Zły wybór')

branch = {'mielonka': 1.25,
          'szynka': 1.99,
          'jajka': 0.99}
print(branch.get('mielonka', 'Zły wybór'))

print(2 > 3) # Porównania wielkości zwracają True/False
print(4 > 3 or [1,2]) # operatory 'and' oraz 'or' zawsze zwracają obiekt
print([] or 3) # analizuje obiekty argumentów od lewej do prawej strony i zwraca pierwszy będący prawdą. Co więcej, po odnalezieniu pierwszego prawdziwego argumentu Python zatrzymuje wyszukiwanie

X = 0
Y = 2
Z = 3
if X:
   A = Y
else:
   A = Z
print(A)

A = Y if X else Z
print(A)
