# 2] create a person class with attributes name and age.then create a subclass employee that adds and attribute salary and a method to display employee detail.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age) 
        self.salary = salary

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)

emp = Employee("Rahul", 25, 30000)

emp.show_details()
