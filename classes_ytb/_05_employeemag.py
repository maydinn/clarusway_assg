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

    def __repr__(self):
        return "Employee ({}, {}, {})".format(self.fist_name, self.last_name, self.pay)

    def __str__(self):
        return "{} - {}".format(self.full_name(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())


emp_1 = Employee("can", "han", 50000)
emp_2 = Employee("ran", "tan", 60000)

print(emp_1)

print(str(emp_1))
print(repr(emp_2))

print(emp_2.__repr__())
print(emp_1.__str__())

print(emp_1 + emp_2)

print(len(emp_1))