import math
"""
Task - 1 :
You work for a manufacturer as a programmer and have been asked
to calculate the total profit made on the sales of a product.
You are given a dictionary (sales) containing the cost price per unit (in dollars),
sell price per unit (in dollars), and the beginning inventory.
Write a program to return the total profit made, rounded to the nearest dollar.
Assume all of the inventory has been sold.
The name and the keys of the dictionary are constant, so use them as they are.
"""

sales = {
    "cost_value": 31.87,
    "sell_value": 45.00,
    "inventory": 1000
}


def total_cost(dictionary):
    return (dictionary['sell_value'] - dictionary['cost_value']) * dictionary['inventory']


print("the profit will be : ", round(total_cost(sales)))

a = float(input("enter a value : "))

print("$" + "%.2f" % a)
