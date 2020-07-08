"""
Task : Find out if the given word is "comfortable words" in relation to the ten-finger keyboard use.

A comfortable word is a word which you can type always alternating the hand you type with
(assuming you type using a Q-keyboard and use of the ten-fingers standard).
The word will always be a string consisting of only letters from a to z.
Write a program to returns True if it's a comfortable word or False otherwise.
"""
from typing import Set, Any

left = set('qwertasdfgzxcvb')
right = set('yuiophjklnm')

"""def comfortable_word(x):
    odd = []
    even = []
    for i in range(0, len(x)):
        if i % 2 == 0:
            even.append(x[i])
        else:
            odd.append(x[i])
    flag = False
    count = 0
    for i in odd:
        if i in RIGHT:
            count += 1
        if i in even:
            count -= 1
    if count == len(odd):
        flag = True

    print(flag)


comfortable_word("clakruskwkay") """

"""LEFT = set('qwertasdfgzxcvb')
RIGHT = set('yuiophjklnm')


def comfortable_word(word):
    one = []
    two = []
    for i, a in enumerate(word):
        if not i % 2:
            one.append(a)
        else:
            two.append(a)
    one = ''.join(one)
    two = ''.join(two)
    return LEFT.issuperset(one) and RIGHT.issuperset(two) or \
           LEFT.issuperset(two) and RIGHT.issuperset(one)


print(comfortable_word('clarusway'))"""

"""def comfortable_word(word):
    one = []
    two = []
    for i, a in enumerate(word):
        if not i % 2:
            one.append(a)
        else:
            two.append(a)
    one = set(one)
    two = set(two)
    return (len(left.intersection(one)) != len(one) and len(right.intersection(one)) != len(one)) or\
           (len(left.intersection(two)) != len(two) and len(right.intersection(two)) != len(two))


print(comfortable_word("tester"))"""

"""word = input("enter a word")
word = set(word)
print(len(left.intersection(word)) != len(word) and len(right.intersection(word)) != len(word))"""

