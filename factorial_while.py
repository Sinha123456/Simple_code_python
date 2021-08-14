number = 6
product = 1
current = 1
while current<=number:
    product*=current
    current += 1
print(product)

#Running same thing using for loop

# calculate factorial of number with a for loop
for num in range(1, number + 1):
    product *= num

# print the factorial of number
print(product)
