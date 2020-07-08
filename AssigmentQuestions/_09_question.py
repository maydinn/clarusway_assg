def cal_risk_covid():
    age = input("Are you a cigarette addict older than 75 years old?: ")
    age = bool_answer(age)
    chronic = input("Do you have a severe chronic disease: ")
    chronic = bool_answer(chronic)
    immune = input("Is your immune system too weak: ")
    immune = bool_answer(immune)
    if age and chronic and immune:
        return "high risk"
    elif age or chronic and immune:
        return "medium risk"
    elif age and chronic or immune:
        return "medium risk"
    elif age or chronic or immune:
        return "low risk"
    else:
        return "no risk"


def bool_answer(answer):
    while True:
        if answer.lower() == "yes":
            return True
        elif answer.lower() == "no":
            return False
        else:
            print("please enter as yes or no, in order to have correct result please refresh the page")
            break


print(cal_risk_covid())
