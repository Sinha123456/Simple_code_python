def list_ends(a_list):
    return [a_list[0], a_list[len(a_list)-1]]
a = [5, 10, 15, 20, 25]
print(list_ends(a))
def fibonacci():
    num = int(input('enter the number you want fibonnaci series\n'))
    i = 1

    if num ==0:
        fib = []
    elif num ==1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num>2:
        fib = [1,1]
        while i < (num-1):
            fib.append(fib[i] + fib[i-1])
            i = i + 1

    return fib

print(fibonacci())






