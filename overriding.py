class parent:
    #print("I am in parent class")
    def __init__(self):
        #print("I am in constructor")
        def filter(self):
            print("It's filter function:")
class child(parent):
    def filter(self):
        print("I am in child class")
class grandchild(child):
    super().__init__()
    def grandvalue(self):
        print("I am in grandchild class")
p = parent()
c = grandchild()
print(c.grandvalue())
#


#another class
class math:
    maths = "numbers"
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
    def sum(self):
        return (self.x1 + self.x2)
    def mul(self):
        return (self.x1*self.x2)
    @classmethod
    def classinfo(cls):
        return cls.maths
    @staticmethod
    def getinfo():
        print("This is math informations")

s = math(2,3)
m = math(3,4)
print(m.mul())
print(s.sum())
print(math.classinfo())
print(math.getinfo())