# types

Built-in Functions 69 important 64
The Python interpreter has a number of functions and types built into it that are always available. They are listed here in alphabetical order.

class object
Return a new featureless object. object is a base for all classes. It has the methods that are common to all instances of Python classes. This function does not accept any arguments.

Note object does not have a __dict__, so you can’t assign arbitrary attributes to an instance of the object class.

object()
type()

@staticmethod()
@classmethod()
super()
issubclass()
isinstance()
property()
hash()
id()
repr()
dir() 
help()
vars()
callable() -> Bool

setattr() 
getattr()
getattr(x, 'foobar') is equivalent to x.foobar
delattr()
hasattr()
The arguments are an object and a string. The result is True if the string is the name of one of the object’s attributes, False if not. (This is implemented by calling getattr(object, name) and seeing whether it raises an AttributeError or not.)

## types
### numeric Types
int() float() complex()

abs()
divmod()
pow()
round()

### iterator types 
### sequence types
list() tuple() range() 
str()

### set types
set()
frozenset()

dict()

bool()

### binary sequence types
bytes()
bytearray()
memoryview()

open()
input()
print()



bin(x:int) -> str
hex(x:int) -> str
oct()
Convert an integer number to a lowercase hexadecimal string prefixed with “0x”.
                      ... to an octal string prefixed with “0o”.
If x is not a Python int object, it has to define an __index__()


slice() -> Range

iter() 
enumerate()
next()
sorted()
reversed()
zip()
map() filter()
all() any()
min() max()

len()
Return the length (the number of items) of an object. 
The argument may be a sequence (such as a string, bytes, tuple, list, or range) or 
a collection (such as a dictionary, set, or frozen set).

format()
# https://docs.python.org/3/library/string.html#formatspec

ascii()
Unicode
chr(i:int) -> str 
ord()

globals() locals()
__import__()



# https://docs.python.org/3/library/functions.html#sum
sum()
breakpoint()
exec()
eval()
compile()












