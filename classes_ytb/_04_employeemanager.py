class Employee:
    raise_amaount = 1.04
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


class Developer(Employee):
    raise_amaount = 1.10

    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
#        Employee.__init__(self, first_name, last_name, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first_name, last_name, pay, employees = None):
        super().__init__(first_name, last_name, pay)
        if employees is None :
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("--->", emp.full_name())


dev_1 = Developer("can", "han", 50000, "Python")
dev_2 = Developer("ran", "tan", 60000, "Java")
mgr_1 = Manager("sue", "smith", 90000, [dev_1])
print(mgr_1.email)
mgr_1.print_emps()
mgr_1.add_emp(dev_2)
mgr_1.print_emps()
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Manager, Developer))
print(issubclass(Manager, Employee))