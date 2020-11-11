def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]





nums = [4,8,1,6,9,5,7]
sort(nums)
print(nums)
