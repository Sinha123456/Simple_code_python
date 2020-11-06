pos = -1
def search(list, n):
    for  i in range(len(list)):
        if list[i] == n:
            globals()["pos"] = i
            return True
            return False
list = [5,4,3,8,9,6,2]
n = 6
if search(list, n):
    print("Found that number at position", pos+1)
else:
    print("Not found")


    