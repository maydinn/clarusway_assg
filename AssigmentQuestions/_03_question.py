# Task-1:
# Write a short Python program that asks the user to enter Celsius temperature
# (it can be a decimal number), converts the entered temperature into Fahrenheit degree and prints the result.
# Task-2:
# Write a short Python program that asks the user to enter a distance (it can be a decimal number) in kilometers,
# converts the entered distance into miles and prints the result.

# Task-1:


def convert_celsius_fahrenheit(celsius):
    celsius = float(input("enter Celsius temperature: "))
    return (celsius/5)*9 + 32


print(convert_celsius_fahrenheit(32))

# Task-2:


def convert_km_mile(km):
    km = float(input("enter km: "))
    return km * 0.62137


print(convert_km_mile(100))

