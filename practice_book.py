def func(a, b = 4, c = 5):
    print(a, b, c)
func(1, 2)
def func(a, b, c = 5):
    print(a, b, c)
func(1, c=3, b=2)
def func(a, *pargs):
    print(a, pargs)
func(1,2,3)
def func(a, **kargs):
    print(a, kargs)
func(a=1, c=3, b=2)
def func(a, b, c=3, d=4):
    print(a,b,c,d)
func(1, *(5,6))
def func(a,b,c): a =2; b[0] = 'x'; c['a'] = 'y'
    
l = 1; m =[1]; n = {'a': 0}
func(l,m,n)
def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])
mysum([1, 2, 3, 4, 5])

