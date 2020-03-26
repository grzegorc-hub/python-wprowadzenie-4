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

print(2 > 3) # True/False
print(2 > 3 or [1,2]) # obiekt
print([] or 3)

X = 1
Y = 2
Z = 3
if X:
   A = Y
else:
   A = Z
print(A)

A = Y if X else Z
print(A)