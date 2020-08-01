class Employee:
    raise_amaount = 1.40
    num_of_emps = 0

    def __init__(self, first_name, last_name, pay):
        self.fist_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + "." + last_name + "@company.com"

        Employee.num_of_emps += 1

    def full_name(self):
        return "{} {}".format(self.fist_name, self.last_name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amaount)


emp_1 = Employee("can", "han", 50000)
emp_2 = Employee("ran", "tan", 60000)

print(emp_1.email)
print(emp_2.email)
print(emp_1.full_name())
print(Employee.full_name(emp_1))
print(emp_2.full_name())
print(Employee.full_name(emp_2))

print((Employee.num_of_emps))

print(emp_1.pay)
print(Employee.raise_amaount)
Employee.apply_raise(emp_1)
print(emp_1.pay)

print(Employee.__dict__)
print(emp_1.__dict__)

Employee.raise_amaount = 1.50
Employee.apply_raise(emp_2)
print(emp_2.pay)

emp_2.raise_amaount = 1.10
Employee.apply_raise(emp_2)
print(Employee.raise_amaount)
print(emp_2.pay)