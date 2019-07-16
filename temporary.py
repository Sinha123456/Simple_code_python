def get_primes():
    num == 2
    while True:
        if is_prime(num):
            yield num
            num += 1
print(get_primes)

def numbers(x):
    for i in range(x):
        if i%2 == 0:
            yield i
print(list(numbers(12)))

def make_word():
    word = ""
    for p in "spam":
        word += p
        yield word
print(list(make_word()))
def decor(func):
    def wrap():
        print("---------")
        func()
        print("---------")
        return wrap
    def print_text():
        print("Hello world!")
        decorated = decor((print_text))
        decorated()
        print_text = decor(print_text)
        print_text()
def print_text():
    print("Hello World")
    print_text = decor(print_text)
@decor
def print_text():
    print("Hello World")
    print_text();

 
     
