# -*- coding: utf-8 -*-
"""dictionary.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gDDe1pTtHRBHyBBQ0J05x01trW04XaPA

1. Write a Python script to sort (ascending and descending) a dictionary by value.
"""

import operator
d = {"b": 2, "c": 3, "a": 1, "d": 4}
sorted_asc = dict(sorted(d.items(), key=operator.itemgetter(1)))
sorted_desc = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print(sorted_asc)
print(sorted_desc)

"""2. Write a Python script to add a key to a dictionary."""

d = {"b": 2, "c": 3, "a": 1, "d": 4}
d["f"] = 6
print(d)

"""3. Write a Python script to concatenate the following dictionaries to create a new one."""

d1 = {"b": 2, "c": 3, "a": 1, "d": 4}
d2 = {"v": 54, "y": 23, "j": 99, "w": 56}
d3 = {"t": 234, "u": 24}
d4 = {}
for i in (d1, d2, d3):
  d4.update(i)
print(d4)

"""4. Write a Python script to check whether a given key already exists in a dictionary."""

d = {"b": 2, "c": 3, "a": 1, "d": 4}
check = "x"
if check in d:
  print("exists already")
else:
  print("not yet")

"""5. Write a Python program to iterate over dictionaries using for loops."""

d = {"b": 2, "c": 3, "a": 1, "d": 4}
for i, index in d.items():
  print(i, "=", index)

"""6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)."""

input = int(input("provide an input:"))
d = dict()
for i in range(1, input + 1):
  d[i] = i * i
print(d)

"""7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys."""

d = dict()
for x in range(1, 16):
  n = x * x
  d[x] = n
print(d)

"""8. Write a Python script to merge two Python dictionaries."""

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"d": 4, "e": 5, "f": 6}
d3 = d1.copy()
d3.update(d2)
print(d3)

"""9. Write a Python program to iterate over dictionaries using for loops."""

d = {"a": 1, "b": 2, "c": 3}
for i, index in d.items():
  print("key:", i, "value:", index)

"""10. Write a Python program to sum all the items in a dictionary."""

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
sum = 0
for i, index in d.items():
  sum += index
print(sum)

"""11. Write a Python program to multiply all the items in a dictionary."""

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
sum = 1
for i, index in d.items():
  sum *= index
print(sum)

"""12. Write a Python program to remove a key from a dictionary."""

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
d.pop("b")
print(d)

"""13. Write a Python program to map two lists into a dictionary."""

list1 = ("one", "two", "three")
list2 = (1, 2, 3)
d1 = dict(zip(list1, list2))
print(d1)

"""14. Write a Python program to sort a given dictionary by key."""

import operator
d = {'a': 1, 'c': 3, 'b': 2, 'd': 4, 'f': 6, 'e': 5}
for x in sorted(d):
  print(x, d[x])

"""15. Write a Python program to get the maximum and minimum values of a dictionary."""

import operator
d = {'a': 1, 'c': 3, 'b': 2, 'd': 4, 'f': 6, 'e': 5, "m": 1000}
maxval = d[max(d, key=d.get)]
minval = d[min(d, key=d.get)]
print("max:", maxval, "min:", minval)

"""16. Write a Python program to remove duplicates from the dictionary."""

d = {'a': 1, "m": 1000, 'c': 3, 'b': 2, 'd': 4, 'f': 6, 'e': 5, "m": 1000, "c":3, 'e': 5}
duplicateindex = []
for x, index in d.items():
  if index in duplicateindex:
    del x
  else:
    duplicateindex.append(index)
print(duplicateindex)

"""17. Write a Python program to check if a dictionary is empty or not."""

d1 = dict()
d2 = {'a': 1, 'c': 3, 'b': 2, 'd': 4, 'f': 6, 'e': 5}
dictlength = len(d2)
if dictlength > 0:
  print("not empty")
else:
  print("empty")

"""18.  Write a Python program to combine two dictionary by adding values for common keys."""

from collections import Counter
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
d2 = {"a": 5, "b": 6, "c": 8, "f": 10}
d3 = Counter(d1) + Counter(d2)
print(d3)

"""19. Write a Python program to get the top three items in a shop."""

import operator
d = {"apple": 100, "orange": 50, "banana": 20, "kiwi": 40, "strawberry": 70}
for x in range(3):
  print(sorted(d.keys(), key=d.get, reverse=True)[x])

"""20. Write a Python program to print a dictionary line by line."""

d = {"apple": 100, "orange": 50, "banana": 20, "kiwi": 40, "strawberry": 70}
for x, index in d.items():
  print(x, index)