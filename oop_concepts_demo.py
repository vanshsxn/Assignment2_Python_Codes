from abc import ABC, abstractmethod

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def info(self):
        return f"{self.name}, {self._age}"

class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new):
        if new < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = new

    def info(self):
        return f"{self.name}, id={self.emp_id}"

class Contractor(Person):
    def __init__(self, name, age, hourly_rate):
        super().__init__(name, age)
        self.hourly_rate = hourly_rate

    def info(self):
        return f"{self.name}, contractor ${self.hourly_rate}/hr"

def print_person_info(p):
    print(p.info())

e = Employee("Alice", 30, "E123", 70000)
c = Contractor("Bob", 28, 40)
print_person_info(e)
print_person_info(c)
print(e.get_salary())
e.set_salary(75000)
print(e.get_salary())
