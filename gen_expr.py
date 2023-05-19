""" Other Comprehension-like Syntax
There are no tuple comprehensions in Python!
    (i + 1 for i in range(10))
While this might look like a tuple comprehension, it's not.
Instead, this syntax can be used to define a generator.
More precisely, this is a generator expression. """


# Generator Expression - AKA Not A Tuple Comprehension
gen_1 = (str(i + 1) for i in range(10))
print(gen_1, "\n")  # Note this doesn't print what you might expect.
print("; ".join(gen_1))  # We need to `consume` the generator
# The thing about Generators is that you can only consume them once!
print("; ".join(gen_1))  # This will print a blank line,
# because this Generator has been emptied in the previous print statement.

# This is the closest thing to a Tuple Comprehension we have in Python
# Technically this is a generator expression passed to the tuple type
tup = tuple(i + 1 for i in range(10))
print(f"{tup = }\n")

""" In Python we can use simular syntax for other computing needs.
Its not always about data structures. """

# Sum Comprehension
# total = sum([i**2 for i in range(10)])  # The extra brackets are not needed
# total = sum((i**2 for i in range(10)))  # The extra parens are not needed
total = sum(i**2 for i in range(10))  # This is the same as above
print(f"{total = }\n")

# Any & All Comprehensions
all_even = all(i % 2 == 0 for i in range(0, 10))
print(f"{all_even = }")  # False
any_even = any(i % 2 == 0 for i in range(0, 10))
print(f"{any_even = }")  # True
