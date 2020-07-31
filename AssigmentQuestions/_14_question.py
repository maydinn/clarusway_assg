def fizz_buzz():
    """
    Print numbers from 1 to 100 inclusively following these instructions:
    if a number is multiple of 3, print "Fizz" instead of this number,
    if a number is multiple of 5, print "Buzz" instead of this number,
    for numbers that are multiples of both 3 and 5, print "FizzBuzz",
    print the rest of the numbers unchanged.
    Output each value on a separate line.
    """
    for i in range(1, 101):
        if i % 15 == 0:
            print(i, "=>", "FizzBuzz")
        elif i % 5 == 0:
            print(i, "=>", "Buzz")
        elif i % 3 == 0:
            print(i, "=>", "Fizz")
        else:
            print(i)


fizz_buzz()
