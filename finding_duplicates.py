#Finding duplicate in a list
#First Method
a = [1,2,2,3,3,1,4,5,6]
import collections
print([item for item, count in collections.Counter(a).items() if count>1])

#Second method
a = (6,7,7,6,8,8,9,0,1)
# b = set()
# c = [x for x in a if x not in b and not  b.add(x)]
# print(c)
# c = set([x for x in a if a.count(x)>1])
# print(c)
#Third Method
from iteration_utilities import duplicates
print(list(duplicates(a)))
#forth method
from iteration_utilities import unique_everseen
print(tuple(unique_everseen(duplicates(a))))
