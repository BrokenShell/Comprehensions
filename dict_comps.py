""" Dictionary Comprehensions """
from string import ascii_uppercase, ascii_lowercase

# Notice that we're flipping the order of char and idx.
# We're doing this because enumerate give us the idx first,
# but we want char to be the key.
dict_comp = {char: idx for idx, char in enumerate(ascii_uppercase[:10])}
print(dict_comp)


# What if we'd like to use some other mapping scheme?
# Uppercase to lowercase for example
a_j_upper = ascii_uppercase[:10]
a_j_lower = ascii_lowercase[:10]
case_map = {k: v for k, v in zip(a_j_upper, a_j_lower)}
print(case_map)
