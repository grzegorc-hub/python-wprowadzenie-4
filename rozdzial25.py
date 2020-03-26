class C2: pass
class C3: pass

class C1(C2, C3):  # Utworzenie i połączenie klasy C1
    def setname(self, who):  # Przypisanie nazwy: C1.setname
        self.name = who  # self to albo I1, albo I2
    def __init__(self):
        print("hello")

I1 = C1()  # Utworzenie dwóch instancji
I2 = C1()
I1.setname('amadeusz')  # Ustawia I1.name na 'amadeusz'
I2.setname('aleksander')  # Ustawia I2.name na 'aleksander'
print(I1.name)  # Wyświetla 'amadeusz'

C1.setname(I2, "olek")
print(I2.name)
