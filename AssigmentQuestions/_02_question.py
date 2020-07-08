# Consider the following questions in terms of True/False regarding someone else.
# Are you a cigarette addict older than 75 years old? Variable → age
# Do you have a severe chronic disease? Variable → chronic
# Is your immune system too weak? Variable → immune
# Set a logical algorithm using boolean logic operators (and/or) and the given variables
# in order to give us True (there is a risk of death) or False (there is not a risk of death) as a result.


def age_risk(age):
    if age > 75:
        return True
    else:
        return False


def death_risk():
    age = int(input("enter your age: "))
    chronic = input("Do you have a severe chronic disease? (please enter as yes or no) ")
    immune = input("Is your immune system too weak? (please enter as yes or no) ")

    if age_risk(age) and chronic.lower() == "yes" and immune.lower() == "yes":
        print("High Risk")
    elif age_risk(age) and chronic.lower() == "yes" or immune.lower() == "yes":
        print("Medium Risk")
    elif age_risk(age) or chronic.lower() == "yes" and immune.lower() == "yes":
        print("Medium Risk")
    elif age_risk(age) or chronic.lower() == "yes" or immune.lower() == "yes":
        print("Low Risk")
    else:
        print("Risk taker")


death_risk()
