# Jak działą importowanie?
# Odnalezienie pliku modułu.
# Skompilowanie go do kodu bajtowego (jeśli jest to konieczne).
# Wykonanie kodu modułu w celu utworzenia definiowanych przez niego obiektów.

# Sciezka szukania modułów:
# 1. Katalog główny programu.
# 2. Katalogi PYTHONPATH (jeśli są ustawione).
# 3. Katalogi biblioteki standardowej.
# 4. Zawartość wszystkich plików .pth (jeśli są one obecne).

import sys
print(sys.path)