
assert 2==2


try:
    with open('data3') as myfile:
        for line in myfile:
            print(line)
except Exception as X:
    print("blad" + str(X.args))
else:
    print('bez bledu')
finally:
    print('koniec')

import sys

def action2():
   print(1 + [])                             # Wygenerowanie wyjątku TypeError

def action1():
   try:
      action2()
   except TypeError:                         # Najbardziej aktualna pasująca instrukcja try
      print(sys.exc_info())
      print('wewnętrzne try')

try:
   action1()
except TypeError:                            # Tutaj tylko jeśli action1 ponownie zgłasza wyjątek
   print('zewnętrzne try')

print(sys.exc_info())