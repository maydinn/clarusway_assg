def prime_numbers():
    num = int(input("enter a number : "))
    liste = list()
    for i in range(2, num):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count += 1
        if count == 0:
            liste.append(i)

    return liste


print(prime_numbers())
