from abc import ABC, abstractmethod
class Mobile(ABC):
    
    def surfing(self):
        pass
class Ipad():

    def surfing(self):
        print("it'Ipad ")
class Smartphone(Mobile):
        def surfing(self):
         print("It's touchscreen")
class Apple(Mobile):
    def surfing(self):
        print("It's Apple phone")
s = Mobile()
y = Ipad()
z = Smartphone()
x = Apple()
print(y.surfing())
print(z.surfing())
