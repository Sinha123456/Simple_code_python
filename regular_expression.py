import re
pattern1 = '951-719-9170ZoeWellish@superrito.com, PamelaSHill@cuvox.de+1 (217) 569-3204'

#s = re.search('[\d\d\d[-]\d\d\d.\d\d\d\d]', pattern1)

# + matches one or more times.
# * matches zero or more times
# ?, matches either once or zero times
# {m,n}, where m and n are decimal integers. This qualifier means there must be at least m repetitions, and at most n
#x = re.findall('[a-zA-Z]', pattern1)
#print(x)
#y = re.findall('\d{3}[-]\d{3}[-]\d{4}', pattern1)

#y = re.search('\d{3}[-]\d{3}[-]\d{4}', pattern1)
#y =re.findall('\D', pattern1)
#y =re.findall('\W', pattern2)
#y =re.findall('[4567]', pattern2)
#y =re.findall('[0-5][0-9]', pattern2) #the string has any two-digit numbers, from 00 to 59
#y =re.findall('[+]', pattern2)
#y = re.sub('\s', '0', pattern2)
#y = str.extract(r'\(?\d{3}\)?[\s-]?\d{3}[\s-]\d{4}', pattern1)

#print(y)

def f(x):
	if x<= 1:
		return 1
	elif x %2 == 0:
		return x * f(x-2)
	else:
		return x * f(x-1)
# how many times call the function
a = [1,3,8]
b = a
b[0] = 5
print(a)