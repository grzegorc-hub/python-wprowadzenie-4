# kazdy obiekt, klasa ma wlasną przestrzeń nazw

# obiekt.atrybut
# WYSZUKIWANIE
# Znajdź pierwsze wystąpienie atrybutu, szukając w obiekcie, a następnie we wszystkich klasach powyżej niego,
# od dołu do góry i od lewej strony do prawej.

class C2:
    x = 3
    z = 5
class C3:
    def __init__(self):
        print("C3 hello")
        self.y = 4
        #self.z = 7

class C1(C2, C3):               # Utworzenie i połączenie klasy C1
    def setname(self, who):     # Przypisanie nazwy: C1.setname
        self.name = who         # self to albo I1, albo I2
    def __init__(self):
        super().__init__()
        print("C1 hello")
        self.x = 11

I1 = C1()                       # Utworzenie dwóch instancji
I2 = C1()
I1.setname('amadeusz')          # Ustawia I1.name na 'amadeusz'
I2.setname('aleksander')        # Ustawia I2.name na 'aleksander'
print(I1.name)                  # Wyświetla 'amadeusz'

C1.setname(I2, "olek")
print(I2.name)

I2.setname("igor")
print(I2.name)

print(I2.x)
print(I2.y)
print(I2.z)