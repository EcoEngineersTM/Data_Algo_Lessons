'''
Given nums of array, n distinct nums in range (0, n),
return one missing num

ex) 
input: nums = [3, 0, 1]
output: 2


1. Selection Sort, Selection Sort, Bubble Sort
- Time O(n^2)

2. Cycle Sort



'''

# Cycle sort
def missingNum_cycleSort(nums):
    for i in range(len(nums)):
        # while nums[i] is not the value to be expected at the spot,
        while nums[i] != i:
            # key => destination idex to which nums[i] should be sent
            key = nums[i]
            if key < len(nums):
            # swap
                nums[i], nums[key] = nums[key], nums[i]

    # after sorting
    for i in range(len(nums)):
        if nums[i] == len(nums):
            return i
    return len(nums)
        

# Total Sum Formula
# we know that actual Num = n(n+1)/2

# [3, 0, 1]
# output : 2
# 0 + 1 + 2 = 3
'''
[3, 0, 1]
totalSum = 1 + 2 + 3 = 6 
actualSum = 4
totalsum - actualsum = 4

'''
def totalSum(nums):
    total_sum = (len(nums) * (len(nums)) + 1)//2
    actual_sum = sum(nums)
    return total_sum - actual_sum
