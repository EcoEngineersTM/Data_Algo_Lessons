# String Topics

## Mutable vs Immutable

## Library Function

## Tries

## Suffix Trie

## SubStrings 

## KMP

## Rabin–Karp algorithm


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


# Sliding Window

## Rabin-Karp Algo

Rabin-Karp Algorithm for Pattern Searching
<https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/>

the Rabin–Karp algorithm or Karp–Rabin algorithm is a string-searching algorithm created by Richard M. Karp and Michael O. Rabin (1987) that uses hashing to find an exact match of a pattern string in a text. It uses a rolling hash to quickly filter out positions of the text that cannot match the pattern, and then checks for a match at the remaining positions. Generalizations of the same idea can be used to find more than one match of a single pattern, or to find matches for more than one pattern.


## KMP Algo

<https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/>

Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m.
