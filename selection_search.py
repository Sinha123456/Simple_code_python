def sort(nums):

    for i in range(6):
        min_value = i
        for j in range(i, 7):
            if nums[j]<nums[min_value]:

                min_value = j


        temp = nums[i]
        nums[i] = nums[min_value]
        nums[min_value] = temp
        print(nums)







nums = [5,3,9,7,6,2, 1]
sort(nums)
print(nums)