# functions
# Table of Contents

1. [Definitions](#definitions)
2. [First function](#create-first-function)
3. [Name convection](#name-convection)
4. [Arguments](#arguments)
5. [Comments](#no-comments-)
6. [How solve task](#how-start-write-code)
7. [Live coding](#live-coding)
8. [Quiz](#quiz)
9. [Testing](#testing)
10. [TDD](#tdd)
11. [Typing](#typing)
12. [Stack & tools](#stack--tools)


## definitions 
Function is:
* a statement or group of statements that together perform a task.
* usually take data, process it, and return a result.  
* easiest way to implement principle DRY (DON'T REPEAT YOURSELF).
* the simpler tool for programmers to write [clean code](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882).

The clean code is code:
* easy to understand.
* easy to modify.
* easy to test.
* works correctly.

## create first function
```python
def say_hello(name):
    print(f'Hello {name}.')

say_hello('Kamil')
```

## name convection
### function
function name:
* verb 
* snake_case
* not too complex
* not shortcuts
* not shadow names build-in

### arguments
name like variables: 
* noun
* snake_case
* short but meaningful ( no one-character variables )
* not shadow names build-in

## arguments
### default
https://docs.python.org/3/tutorial/controlflow.html#default-argument-values
### keywords
https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments
### arbitrary argument lists
https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists

## NO COMMENTS !!!
no comments to hard to maintain 
exceptions: 
* [doctests](https://docs.python.org/3/library/doctest.html) -> [pytest + doctests](https://docs.pytest.org/en/stable/doctest.html)
* code is very complex, math operations
* useful links, readme is good place too

## HOW START WRITE CODE?
HOW WRITE FUNCTIONS? 
HOW SOLVE PROBLEMS? 

If You have complex problem just draw flowchart than code, code, code.

For example flowchart representing a process for dealing with a non-functioning lamp.

![Alt text](./images/flowchart.png?raw=true "Title")

## LIVE CODING     

## quiz 

Question 1.
Function usually take data, process it, and return a result.
What result return this function? 

Question 2.
![Alt text](./images/flowchart.png?raw=true "Title")

[lamp algorithm implementation](lamp.py)
<details><summary>implementation</summary>
<p>

```python
def is_plugged_in():
    pass


def plug():
    pass


def is_bulb_burned_out():
    pass


def replace_bulb():
    pass


def repair():
    pass


if is_plugged_in():
    plug()
else:
    if is_bulb_burned_out():
        replace_bulb()
    else:
        repair()
```
</p>
</details>

### It's good implementation? What can be wrong with this code?

<details><summary>ANSWER</summary>
<p>
Tooo much functions, maybe something is trivial and not need functions, maybe not need test 
</p>
</details>

## Testing

## TDD
Better practice than just code code code is Test Driven Development.
Example [tic tac toe](https://github.com/KuligKamil/tic-tac-toe/tree/engine)

## typing

## Stack / Tools
[pytest](https://docs.pytest.org/en/stable/)
Pycharm <- [Detect duplicates on the fly](https://www.jetbrains.com/help/pycharm/analyzing-duplicates.html#detect-duplicates)
[mypy](https://mypy.readthedocs.io/en/stable/) 