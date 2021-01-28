# https://docs.python.org/3/library/stdtypes.html
from typing import List


def a() -> List:
    pass


examples = [
    1,
    3.14,
    complex(),
    bool(),  # False
    'text',
    {},
    [],
    (),
    set(),
    frozenset(),
    None
]

# range
examples_with_dir = {}
# type return type of an object
for example in examples:
    # type(example)
    print(type(example))
    print(dir(example))
    examples_with_dir[type(example)] = dir(example)

result = set(examples_with_dir[type(examples[0])])
for example in examples_with_dir.values():
    list1_as_set = set(example)
    intersection = list1_as_set.intersection(result)
    result = intersection

for key in examples_with_dir.keys():
    examples_with_dir[key] = set(examples_with_dir[key]) - set(result)
    list(examples_with_dir[key]).sort()

examples_with_dir2 = {}
# type return type of an object
for example in examples:
    # type(example)
    print(type(example))
    print(dir(example))
    examples_with_dir2[type(example)] = dir(example)

intersections_result = {}
result = set(examples_with_dir[type(examples[0])])
for key, value in examples_with_dir.items():
    for key2, value2 in examples_with_dir.items():
        if key != key2 and (
                f'{key} {key2}' not in intersections_result and f'{key2} {key}' not in intersections_result):
            intersections_result[f'{key} {key2}'] = value.intersection(value2)

# help(1['__abs__'])
import pprint, inspect

pp = pprint.PrettyPrinter(indent=4)

a = inspect.getmembers(1)
pp.pprint(a)
inspect.getdoc(a)
pp.pprint(a)

pp.pprint(intersection)


def do_it(number: int):
    print(number)
    number = 'sdadasda'
    print(number)
    f = 7
    # f.

# types
# basic
# complex

# mutable
# immutable
# str immutable
#
# iterator
# Sequence

# https://docs.python.org/3/library/collections.html

# convert from str to int
# https://www.educative.io/edpresso/what-are-mutable-and-immutable-objects-in-python3

# https://www.geeksforgeeks.org/mutable-vs-immutable-objects-in-python/

# https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747

# https://www.youtube.com/watch?v=pMgmKJyWKn8&ab_channel=PyCon2018
