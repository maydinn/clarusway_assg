class Employee:
    age = 20
    def __init__(self, first_name, last_name):
        self.fist_name = first_name
        self.last_name = last_name
        # self.email = first_name + "." + last_name + "@company.com"

    @property
    def email(self):
        return "{}.{}@company.com".format(self.fist_name, self.last_name)

    @property
    def full_name(self):
        return "{} {}".format(self.fist_name, self.last_name)

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(" ")
        self.fist_name = first
        self.last_name = last

    @full_name.deleter
    def full_name(self):
        print("Deleted")
        self.fist_name = None
        self.last_name = None


emp_1 = Employee("john", "smith")

print(emp_1.fist_name)
print(emp_1.email)
print(emp_1.full_name)

emp_1.fist_name = "kat"

print(emp_1.fist_name)
print(emp_1.email)
print(emp_1.full_name)

emp_1.full_name = "jim karter"

print(emp_1.fist_name)
print(emp_1.email)
print(emp_1.full_name)

hume = Employee("ali", "can")
hume.age = 25
print(Employee.age)
print(hume.age)