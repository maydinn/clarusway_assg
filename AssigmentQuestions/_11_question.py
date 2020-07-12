def prime_number():
    """
     a function that takes a number from the user and prints the result to check if it is a prime number.
     prime number: a number that is divisible only by itself and 1
    """
    n = int(input("enter a number: "))
    count = 0
    for i in range(1, n + 1):
        if not (n % i): count += 1
    if n == 0 or n == 1 or count >= 3:
        print(n, "is not a prime number")
    else:
        print(n, "is a prime number")


prime_number()
