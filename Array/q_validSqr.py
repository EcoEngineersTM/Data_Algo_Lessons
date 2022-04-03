'''
Given input of Nums return if the nums can be squared. Combine numbers if needed to form Square(geometry)

ex)
nums = [1, 1, 2, 2, 2]
        |  |
         2    2  2 2  => True
    
ex 2)

        |
nums = [3, 3, 1, 2, 2, 4, 1]
len(nums) = 7
sum(nums) = 16

sum/4 = 4
len(wall) = 4

4 - 3 = 1
        |      |
nums = [ 2, 2  ]
output = [4, 4, 4, 4]
check if len(output) == 4:

16
4
 l        r
 |        |
[1, 2, 2, 3, 4]
[4, 3, 2,2 ,1]
 |

if num

output = []
key = 4
Things To Consider
* each num must be less than key = sum//4 < 4
for num in nums:
    if num > key:
        return False 
    if num == key:
        output.append(num)
    sum = l + r
    if l + r
        


* len(output) == 4
* ouput = []
* get sum of nums;
    nums.sum()
* Sort the nums
    nums.sort()




[4, 4, 4, 4] 
       |   | 
         r
if num == key:
    continue
while num != key:
    nums[i] += nums[right]
    nums.pop()
'''


nums = [3, 3, 1, 2, 2, 4, 1]


# found how to return Output
def findAlgo(nums):
    nums.sort(reverse=True)
    key = sum(nums)/4
    output = []

    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[left] == key:
            output.append(nums[left])
            left += 1

        # condition if left > key => return FAlse

        else:
            nums[left] += nums[right]
            right -= 1

    return output


print(findAlgo(nums))

nums2 = [3, 3, 1, 2, 2, 4, 1]

# without using output
def findsqr(nums):
    nums.sort(reverse=True)
    key = sum(nums)/4

    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[left] == key:
            left += 1
        # condition if left > key => return FAlse
        elif nums[left] > key:
            return False

        else:
            nums[left] += nums[right]
            right -= 1
            nums.pop()

    return len(nums) == 4


print(findsqr(nums2))
            
