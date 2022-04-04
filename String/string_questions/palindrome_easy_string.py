'''
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
 and removing all non-alphanumeric characters, it reads the same forward and backward. 
 Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''

# method 1 Two Pointers

'''
Python String isalnum()
The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers). 
If not, it returns False.


1. create output list to return
2. create two pointers, left = 0 & right = s[len(s)]
3. while left < right:
    check if left != right:
        return False
4. Return True
'''

# Time: O(n)
# Space: O(1)
def palindromeImmutable(s):
    left = 0 
    right = len(s)-1

    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1


s = 'noon'

print(print(palindromeImmutable(s)))
