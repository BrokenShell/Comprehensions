""" List Comprehensions
- Basic Comprehension
- Transform
- Filter
- Transform & Filter
- Performance
"""
from typing import List
from MonkeyScope import timer


# Basic List Comprehension
arr_0 = [i for i in range(10)]
print(arr_0)
# For such a simple procedure it's actually better to do this: `list(range(10))`


# Transform - Plus one, this replaces `map`
arr_1 = [i + 1 for i in range(10)]
print(arr_1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Filter - Even numbers only, this replaces `filter`
arr_2 = [i for i in range(10) if i % 2 == 0]
print(arr_2)  # [0, 2, 4, 6, 8]


# Transform & Filter - Square of Evens
# Notice how the filter happens first - very efficient
# Also notice that we do not get an `else` clause here
arr_3 = [i**2 for i in range(10) if i % 2 == 0]
print(arr_3)  # [0, 4, 16, 36, 64]


# Performance Analysis

def make_list(n: int) -> List[int]:
    result = []
    for i in range(n):
        result.append(n)
    return result


def make_comp(n: int) -> List[int]:
    return [i for i in range(n)]


if __name__ == '__main__':
    # Performance will vary from one machine to another
    timer(make_list, 1000)  # Typical Timing: 49567 ± 941 ns
    timer(make_comp, 1000)  # Typical Timing: 23358 ± 734 ns
