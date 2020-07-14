def fact():
    my_list = list()
    a = 0
    b = 1
    for i in range(5):
        b = b + a
        my_list.append(b)
        a = b + a
        my_list.append(a)
    return my_list


print(fact())
