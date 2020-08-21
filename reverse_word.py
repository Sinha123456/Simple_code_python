
'''def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
s = "Geeksofgeeks"
print(reverse(s))'''
'''def reverse(str):
    str = str[::-1]
    return str
sent = "My name is neetu, try to print reverse string"
print(reverse(sent))'''
def reverse(str):
    str = "".join(reversed(str))
    return str
print(reverse("coding is fun"))