import dir1.dir2.mod       # Pierwszy import wykonuje pliki inicjalizacyjne
import dir1.dir2.mod       # kolejne importy juz tego nie robią

print(type(dir1))
print(type(dir1.dir2.mod))
print(dir1.x)
print(dir1.dir2.y)
print(dir1.dir2.mod.z)

from dir1.dir2 import mod
print(mod.z)
mod.z = 4

import dir1.dir2.mod as myMod
print(myMod.z)

