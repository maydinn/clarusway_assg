"""
Task : Find out the most frequent number and its frequency.

Write a program that;

Finds out the most frequent number in the given list.
Calculates its frequency.
Prints out the result such as :
"""

my_list = [1, 3, 7, 4, 3, 0, 3, 6, 3]
a = 1
d = 0
for i in my_list:
    b = my_list.count(i)
    if a < b:
        d = i
    a = b
    b = a

print("the most frequent number is", d, "and it was", my_list.count(d), "times repeated")
