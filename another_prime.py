check_prime = [26, 39, 51, 53, 57, 79, 85]
for num in check_prime:
    for i in range(2,num):
        if (num%i) == 0:
            print('{} is not a prime because {} is a factor of {}'.format(num, i, num))
            break
        if i == num-1:
            print('{} number is prime'.format(num))

