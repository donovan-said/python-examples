""" Sample List Comprehensions
* https://www.w3schools.com/python/python_lists_comprehension.asp
* https://www.programiz.com/python-programming/list-comprehension

List comprehension offers a shorter syntax when you want to create a new list
based on the values of an existing list.
"""

"""
--------------------------------------------------------------------------------
Syntax:

newlist = [expression for item in iterable if condition == True]

The return value is a new list, leaving the old list unchanged.
"""

# EXAMPLE: Create a new list using list comprehension

numbers = [1, 2, 3, 4]

square_numbers = [num * num for num in numbers]

print(square_numbers)

# EXAMPLE: Conditionals in List Comprehension

# Filtering even numbers from a list
even_numbers = [num for num in range(1, 10) if num % 2 == 0]

print(even_numbers)

# EXAMPLE: List Comprehension with String

word = "Python"
vowels = "aeiou"

# find vowel in the string "Python"
result = [char for char in word if char in vowels]

print(result)
