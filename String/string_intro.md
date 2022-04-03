# String Topics

## Mutable vs Immutable

## Library Function

## Tries

## Suffix Trie

## SubStrings 

## KMP

## Rabin Karp


# Easy Questions

## Reverse a String

### Check if a String is a Palindrome

# Type of Questions

## Immutable vs Mutable

### Immutable

- In python:
- Modification: strings.copy()

### Mutable

- can be change inplace
- modification: inplace

## Return Reverse

### Immutable Approach

```
Reverse
input: 'Moon'
output: 'nooM'
```

Algorithms

1. create output
2. iterate right to left & append num to output
3. return output

### Mutable Approach

1. Create two pointers: left & right
2. while left <= right: Swap

## find Palindrome

- must be mirror

- ex

```
// Palindrome
'moom'

// not Palindrome
'Moon'
```

Algorithm 1

1. create two pointers, left & right
2. compare

Algorithm 2

1. create two pointers in median & median + 1
2. compare


## Substring Match Questions
Given String & Sub, check if Sub is substring of String

### Method 1:Enumeration (Check all possibility)
Time: O(n^2)

### Method 2: Sliding Window
- checking contiguous sub-array or sub-strings