class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        return "{} is {} years old" .format(self.name, self.age)
    def speak(self, sound):
        return "{} says {}" .format(self.name, sound)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}" .format(self.name, speed)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}" .format(self.name, speed)
jim = Bulldog("jim", 12)
print(jim.description())
print(jim.run('slowly'))
print(jim.speak('woo'))
# is jim is instance of Dog()?
print(isinstance(jim, Dog))
julie = Dog("Julie", 100)
print(isinstance(julie, Dog))
johnnywalker = RussellTerrier("Johnnywalker", 4)
print(isinstance(johnnywalker, Bulldog))

class Computer:
    def __init__(self):
        self.name = 'Neetu'
        self.age = 20
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False
c1 = Computer()
c1.age = 30
c2 = Computer()
if c1.compare(c2):
    print("They are same")
else:
    print("They are different")
class Student:
    school = 'Purdue'
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def avg(self):
        return(self.m1 + self.m2 + self.m3)/3
    
    def info(cls):
        return cls.school


s1 = Student(45, 60, 80)
s2 = Student(50,30,90)
print(s1.avg())
print(s1.info())    
        


                    


