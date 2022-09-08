# Labs Data Science Workshop: Python Comprehensions

### Workshop Outline
0. Introduction & Motivation
1. List Comprehensions
2. Set Comprehensions
3. Dictionary Comprehensions
4. Generator Expressions

## 0. Introduction & Motivation
Comprehensions are one of the most useful features to come from Python. They make our
code more condensed and readable than the for loops they replace. When
Comprehensions were first introduced they lacked some performance, but today they're
just as performant as a for loop, in fact in many cases - they're faster!

But it's not about performance or efficiency - it's more about writing beautiful
code. It's about being Pythonic by writing declarative rather than imperative
code.

- Imperative: tell Python how to do something, step by step.
- Declarative: tell Python what to do, but let Python decide how.

## 1. List Comprehensions
List comprehensions replace many varieties of for-loops that seek to populate a
list via iteration. List comprehensions do the same thing but with Pythonic style.
In addition to allowing us to create simple lists we can also use List Comprehensions to do mapping and filtering. In fact, it's entirely possible to solve the popular FizBuzz coding challenge with one list comprehension.

### Simple List Comprehension

```
arr = [i for i in range(10)]
arr
```

Same resulting list as the next cell, but this isn't as good as the other one - it's not as "Pythonic".

```
arr = []
for i in range(10):
    arr.append(i)
arr
```

### A List Comprehensions can replace `map`
In this example we're mapping the integers from 0-9 to strings

```
arr = [str(i) for i in range(10)]
arr
```

Same as this...

```
arr = list(map(str, range(10)))
arr
```

Same as this for-loop code also... but this for-loop variant is considered ugly compared to the other two.

```
arr = []
for i in range(10):
    arr.append(str(i))
arr
```

### List Comprehensions can replace `filter`
Here we're filtering out integers that aren't evenly dividable by 3

```
arr = [i for i in range(10) if i % 3 == 0]
arr
```

### List Comprehensions can even replace `map` and `filter` at the same time
Mapping integers to strings if the number is evenly dividable by 3

```
arr = [str(i) for i in range(10) if i % 3 == 0]
arr
```

#### This time with even more complexity

- If the number is evenly dividable by 3 include it as a string
- If the result is not also evenly dividable by 2 we'll instead get "NOPE"

```
arr = [str(i) if i % 2 == 0 else "NOPE" for i in range(10) if i % 3 == 0]
arr
```

Same as...

```
def transform(value: int) -> str:
    if value % 2 == 0:
        return str(value)
    else:
        return "NOPE"

print(list(map(transform, filter(lambda x: x % 3 == 0, range(10)))))
```

Same as this too... but this one is terribly ugly. Pythonistas don't write code like this.

```
arr_1 = []
for i in range(10):
    if i % 3 == 0:
        if i % 2 == 0:
            arr_1.append(str(i))
        else:
            arr_1.append("NOPE")

print(arr_1)
```

As an exercise - try using a list comprehension to solve FizBuzz.
FizBuzz:
Iterate from 1 to 100
If the number is evenly dividable by 3 print Fiz
If the number is evenly dividable by 5 print Buzz
If the number is evenly dividable by both 3 and 5 print FizBuzz
Otherwise print the number

***5-Minute Timer***

```
fizz_buzz = [
    "FizzBuzz" if i % 15 == 0
    else "Fizz" if i % 3 == 0
    else "Buzz" if i % 5 == 0
    else str(i)
    for i in range(1, 101)
]
print("\n".join(fizz_buzz))
```

### Check for Understanding
1. True or False. A list comprehension is slower than a for-loop that produces the same list?
2. True or False. If I need to filter and/or transform values while constructing a list, I can use a list comprehension instead of a for-loop.

### CFU Answers
1. False. In recent versions of Python, comprehensions have better performance.
2. True. List comprehensions can replace both filter and map.

## 2. Set Comprehensions
This works just like a list comprehension, but produces a set instead. The only difference is the style of brackets used.

```
set_1 = {str(i) for i in range(10) if i % 2 == 0}
set_1
```

The following produces the same result, but it's slightly better, utilizing a fancy range with (start, stop, step)

```
set_1 = {str(i) for i in range(0, 10, 2)}
set_1
```

### Check for Understanding
1. True or False. Set comprehensions are expressed the same as list comprehensions but with curly brackets instead of square brackets.
2. True or False. Sets created with a comprehension do not support set methods like regular sets; union for example.

### CFU Answers
1. True. They can support all the same filter and mapping features as well.
2. False. Set comprehensions produce real sets with all the usual bells and whistles of sets.

## 3. Dictionary Comprehensions

### Dictionary Comprehension with Enumerate
We've seen enumerate already, to spice things up - let's start enumerating at 10

```
dic = {k: v for k, v in enumerate(range(10), 10)}
dic
```

### Dictionary Comprehension with Zip
Mapping Uppercase to Lowercase

```
from string import ascii_uppercase, ascii_lowercase
```

Using the string library and a slice to get the first 10 letters of the alphabet, A-J

```
upper_arr = ascii_uppercase[:10]
lower_arr = ascii_lowercase[:10]

print(f"{upper_arr=}")
print(f"{lower_arr=}")
```

Zip, like enumerate, works with any Iterable - including lists, strings, tuples and more!

```
alpha_dict = {k: v for k, v in zip(upper_arr, lower_arr)}
alpha_dict
```

### Check for Understanding
1. True or False. You must import a special library to do Dictionary Comprehensions
2. True or False. Typically, in a dictionary comprehension `k` and `v` are variable names for a key and value of the dictionary.


### CFU Answers
1. False. Dictionary comprehensions are built into Python.
2. True. Comprehensions are one place where super short variable names are quite common.

## 4. Generator Expression or Not A Tuple Comprehension
 - A Generator is a type of Iterator
 - All Generators are Iterators, but not all Iterators are Generators
 - Iterators and Generators will remember where you leave off if you stop iterating early
 - We'll have a future Workshop about Iterators and Generators

Generator expressions look like they should be tuple comprehensions, but they do not create tuples. Python does not have tuple comprehensions, instead we have generator expressions.

First lets see how generators can be a bit confounding at times, and what to do about it. Notice the following cell doesn't print what you might expect. This is due to the fact that Iterators are lazy...in a good way! Also notice in the cell below we need to wrap the generator expression in parens. This is only required when the resulting code would be ambiguous or violate regular Python syntax without them.

```
gen = (str(i) for i in range(10) if i % 2 == 0)
gen
```

To get the items out, we need to unpack them by iterating through the iterator or by casting to non-lazy type. Yet another way is to use the star operator.

```
for item in gen:
    print(item)
```

Notice the following cell doesn't print anything at all,
because the generator has been fully consumed in the previous cell.

```
for item in gen:
    print(item)
```

The following shows another way to write a simple Iterator

```
iterator = iter(range(10))
```

Just 0-4

```
for item in iterator:
    print(item, end=", ")
    if item >= 4:
        break
```

And then later 5-9, this time with the star operator

```
print(*iterator, sep=", ")
```

Notice the following won't print anything,
just like the generator in a previous example, this iterator has been fully consumed!

```
for item in iterator:
    print(item)
```

Note in the cell below we need to surround the generator expression with parens. This is to differentiate it from the star operator that comes before it.

```
print(*(str(i) for i in range(10) if i % 2 == 0))
```

Using a generator expression is generally better than constructing a list or tuple. This works for all functions that take an Iterable as input. This technique requires far less RAM, but it's also more elegant. In the code below we'll see two examples (`join` and `sum`), there are many others that work the same way, `any`, `all`, `min` and `max` for example.

### Join with a Generator

```
print(", ".join(str(i) for i in range(10)))
```

### Sum with a Generator
Sum the squares of even numbers from 0 to 9

```
total = sum(i**2 for i in range(10) if i % 2 == 0)
print(f"{total = }")  # Notice the spaces around `=` are maintained
```

### Check for Understanding
1. True or False. Tuple Comprehensions are just like list comprehensions but with parens instead of square brackets.
2. True or False. Generator Expressions must have surrounding parenthesis.
3. True or False. Sum is supposed to take a sequence, so you must first transform a generator expression into a list or tuple to use it with `sum`.

### CFU Answers
1. False. Python does not have Tuple Comprehensions.
2. False. You only use parens when the generator expression needs them. For example when you want to assign it to a variable, or use the star operator to unpack it immediately or any other time Python can't otherwise tell where it begins and ends.
3. False. Passing a generator expression to a builtin function is generally better than constructing a list first.
