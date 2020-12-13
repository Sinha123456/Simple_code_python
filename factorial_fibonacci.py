def factorial(n):
    x = 1
    for i in range(1, n+1):
        x = x*i
    return x

print(factorial(5))


def fibonnaci(num):
    a = 0
    b = 1
    if num ==1:
        print(a)
    elif num<0:
        print('Number is invalid')
    else:
        print(a)
        print(b)

        for i in range(2,num):
            c = a+b
            a = b
            b = c
            print(c)
x = fibonnaci(8)
print(x)