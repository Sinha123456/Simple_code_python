pos = -1
def search(list, n):
    lowerbond = 0
    upperbond = len(list)
    while lowerbond<= upperbond:
        mid = (lowerbond + upperbond) // 2
        if list[mid] == n:
            globals()['position'] = mid
            return True
            return False
        else:
            if list[mid] < n:
                lowerbond = mid
            else:
                upperbond = mid
        return False

list = [3,5,8,11,22,32,34,45,55]
n = 22
if search(list,n):
    print("number found at position", position+1)
else:
    print("not found")
