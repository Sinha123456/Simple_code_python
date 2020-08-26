import random
#one type solution to genrate password
charcters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%?&*^()"
passlen = 7
password = "".join(random.sample(charcters, passlen))
print(password)
import string

def pwd():
    pwd = ""
    count = 0
    length = int(input("how many characters do you want in your password "))
    while count != length:
        upper = [random.choice(string.ascii_uppercase)]
        lower = [random.choice(string.ascii_lowercase)]
        num = [random.choice(string.digits)]
        symbol = [random.choice(string.punctuation)]
        all = upper+lower+num+symbol
        pwd = pwd + random.choice(all)
        count = count + 1
        continue
    if count == length:
        print(pwd)
print(pwd())




