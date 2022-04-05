
# given nums = [4, 7, 2, 9], and targetSum = 
'''
given nums = [4, 7, 2, 9], and targetSum = 11
create a function which return two numbers that sum up to targetSum

Three Different Solution. make sure explain time & space complexity
'''

# Brute Force (Enumeration)

def twoSum(nums, targetSum):
  for i in range(len(nums) -1):
    for j in range(i +1, len(nums)):
      first = nums[i]
      second = nums[j]
      print([first, second])


# Optmial Solution 1


# Optimal Solution 2
