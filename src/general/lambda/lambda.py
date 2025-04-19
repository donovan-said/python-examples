""" Sample Lambda functions
* https://www.w3schools.com/python/python_lambda.asp

A lambda function is a small anonymous function. A lambda function can take any
number of arguments, but can only have one expression.
"""

"""
--------------------------------------------------------------------------------
Syntax:

lambda arguments : expression
"""

# EXAMPLE: The expression is executed and the result is returned

x = lambda a: a + 10
print(x(5))

# EXAMPLE: Lambda functions can take any number of arguments:

y = lambda a, b: a * b
print(y(5, 6))

# EXAMPLE: Summarize argument a, b, and c and return the result

z = lambda a, b, c: a + b + c
print(z(5, 6, 2))

"""
--------------------------------------------------------------------------------
Why Use Lambda Functions?

The power of lambda is better shown when you use them as an anonymous function
inside another function.

Say you have a function definition that takes one argument, and that argument
will be multiplied with an unknown number:
"""


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


def myString(x):
    return lambda a: (
        f"Argument passed into lambda is {a}"
        + f"Argument passed into function is: {x}"
    )


funcString = myString("FUNCTION STRING")

print(funcString("LAMBDA STRING\n"))
