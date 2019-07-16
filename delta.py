def this_is_example(myarg1):
    return myarg1
def this_is_another_example(myarg):
    return this_is_example(myarg)
this_is_another_example(1)
print(this_is_example)

def my_school(fun):
    return fun
def homework(terrible):
    return my_school(fun)
print(my_school)
def square(x):
    return x*x
def cube(x):
    return x*x*x
def result(x, func):
    return func(x)
do_square = square
do_cube = cube
res = result(5, do_square)
print(res)
res = result(5, do_cube)
print(res)

