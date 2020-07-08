def armstrong_number():
    print("welcome to armstrong number checker")
    num = check_number()
    power = len(num)
    sum_num = 0
    for i in num:
        sum_num += int(i) ** power
    if int(num) == sum_num:
        return num + " is an Armstrong number"
    else:
        return num + " is not an Armstrong number"


def check_number():

    while True:
        num = input("enter a number: ")
        if num.isalpha():
            print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
        elif ("," in num) or ("." in num):
            print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
        elif float(num) < 0:
            print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
        else:
            return num


print(armstrong_number())
