[resources](https://realpython.com/python-coding-interview-tips/#select-the-right-built-in-function-for-the-job)
# Must Know Python for Data & Algo


## Use enumerate() to iterate over both indices and values
    1. get each element’s index and value at the same time
    2. For each element, enumerate() returns a counter and the element value. 
```
>>> numbers = [45, 22, 14, 65, 97, 72]
>>> for i, num in enumerate(numbers, start=52):
...     print(i, num)
...
52 45
53 22
54 14
55 65
56 97
57 72
```

## Use List Comprehensions Instead of map() and filter()
### ex
- [square(x) for x in numbers]
- [x for x in numbers if is_odd(x)]

# Debug problematic code with breakpoint()

- Python 3.7, you don’t need to import anything and can just call breakpoint()


# Format strings effectively with f-strings
  ```
  >>> def get_name_and_decades(name, age):
...     return f"My name is {name} and I'm {age / 10:.5f} decades old."
...
>>> get_name_and_decades("Maria", 31)
My name is Maria and I'm 3.10000 decades old.
  ```

# Sort lists with custom arguments
- By passing in a lambda function that returns each element’s age, you can easily sort a list of dictionaries by a single value of each of those dictionaries. In this case, the dictionary is now sorted in ascending order by age.

```
>>> sorted([6,5,3,7,2,4,1])
[1, 2, 3, 4, 5, 6, 7]

>>> sorted(['cat', 'dog', 'cheetah', 'rhino', 'bear'], reverse=True)
['rhino', 'dog', 'cheetah', 'cat', 'bear]
```


- Use generators instead of list comprehensions to conserve memory
- Define default values when looking up dictionary keys
- Count hashable objects with the collections.Counter class
- Use the standard library to get lists of permutations and combinations
