t = (1,2,3)
l=[1,2,3]
d={1:'a',2:'b',3:'c'}

print ('list is  ',l)
print ('tuple is ',t)
print('dict is ',d)

def knights(saying):
    def inner(quote):
        print (saying)
        return "We are the knights who say: '%s'" % quote
    return inner(saying)
#print(knights(1))
#print(saying)

def infinite_seven():
    
    while True:
        yield 7
        
        for i in infinite_seven():
            print(i)

infinite_seven(1)
