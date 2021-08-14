# for _ in range(5):
#     print(_)

# languages = ["Python", "JS", "PHP", "Java"]
# for _ in languages:
#     print(_)
    #print(languages)
# _ = 5
# while _ <10:
#     print(_, end = ' ')
#     _ += 1

# def func():
#     return 'datacamp'
# def private_func():
#     return 7
#print(func())

#double underscore

# class Sample():
#
#     def __init__(self):
#         self.a = 1
#         self._b = 2
#         self.__c = 3
# class SecondClass(Sample):
#
#     def __init__(self):
#         super().__init__()
#         self.a = "overridden"
#         self._b = "overridden"
#         self.__c = "overridden"
# obj2 = SecondClass()
# print(obj2.a)
# print(obj2._b)
# print(obj2.__c)
class SimpleClass:

    def __init__(self):
        self.__datacamp = "Excellent"

    def get_datacamp(self):
        return self.__datacamp

obj = SimpleClass()
print(obj.get_datacamp()) ## it prints the "Excellent" which is a __var
print(obj.__datacamp)     ## here, we get an error as mentioned before. It changes the name of the variable