def prime_number(x):
    """
     a function that takes a number from the user and prints the result to check if it is a prime number.
     prime number: a number that is divisible only by itself and 1
    """
    for i in range(2, x):
        if x % i:
            return f"{x} is a prime number"
        else:
            return f"{x} is not a prime number"


print(prime_number(10))
