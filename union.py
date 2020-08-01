'''a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([num for num in a if num<5])
import matplotlib.pyplot as plt
fig = plt.figure()
fig, ax = plt.subplots()
fig, axs = plt.subplots(2,2)
plt.show()'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in b:
    if i in a:
        c.append(i)
print(c)