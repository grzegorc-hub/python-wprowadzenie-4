# with wyrażenie [as zmienna]:
#    blok_with

# 1. Wyrażenie jest analizowane, w wyniku czego otrzymujemy obiekt znany jako menedżer kontekstu (ang. context manager), który musi zawierać metody __enter__ oraz __exit__.
# 2. Wywołana zostaje metoda __enter__ menedżera kontekstu. Wartość przez nią zwracana jest przypisywana do zmiennej w części as, jeśli jest ona obecna. W przeciwnym razie jest ona usuwana.
# 3. Wykonywany jest kod w zagnieżdżonym bloku with.
# 4. Jeśli blok ten zwraca wyjątek, wywołana zostaje metoda __exit__(typ, wartość, ślad) zawierająca szczegóły wyjątku. Warto zauważyć, że są to te same wartości, które są zwracane przez sys.exc_info, opisane w dokumentacji Pythona oraz nieco później w tej części książki. Jeśli metoda ta zwraca wartość będącą fałszem, wyjątek jest zgłaszany ponownie. W przeciwnym razie wyjątek jest kończony. Wyjątek normalnie powinien być zgłoszony ponownie w celu przekazania go poza instrukcję with.
# 5. Jeśli blok nie zgłasza wyjątku, metoda __exit__ nadal jest wywoływana, jednak do jej argumentów typ, wartość oraz ślad przekazywane są obiekty None.

class TraceBlock:
   def message(self, arg):
      print('wykonywanie', arg)
   def __enter__(self):
      print('rozpoczęcie bloku with')
      return self
   def __exit__(self, exc_type, exc_value, exc_tb):
      if exc_type is None:
         print('normalne wyjście\n')
      else:
         print('zgłoszenie wyjątku!', exc_type)
         return False                                 # Przekazanie

with TraceBlock() as action:
   action.message('test 1')
   print('osiągnięty')

with TraceBlock() as action:
    action.message('test 2')
    raise TypeError
    print('nie został osiągnięty')
