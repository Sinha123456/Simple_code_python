str_val =  str(input("enter the string , see that's palindorme or not.\n"))
word = str_val[::-1]
print(word)
if str_val == word:
    print("That's word is palindorme.")
else:
    print("That word is not a palindrome")
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [num for num in a if num%2==0]
print(b)
x = []
for num in a:
    if num%2 == 0:
        x.append(num)
print(x)
