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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amaount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

emp_1 = Employee("can", "han", 50000)
emp_2 = Employee("ran", "tan", 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amaount)
print(emp_2.raise_amaount)
print(emp_1.raise_amaount)


emp_str1 = "John-Doe-70000"
new_emp_1 = Employee.from_string(emp_str1)
print(new_emp_1.email)