import math
def calpie(roundval):
    pieval = round(math.pi,roundval)

    return pieval
number = int(input("Enter the number of digits you want after the decimal."))
try:
    print(calpie(number))
except:
    print("number is not valid")
