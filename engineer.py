# Create an engineer class that inherita property from employee and has additional attributes : name and age

class employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showdetails(self):
        print("role = ", self.role)
        print("dept = ", self.dept)
        print("salary =", self.salary)

class engineer(employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age

        super().__init__("Engineer", "IT", "75000")

eng1 = engineer("Jenny", 45)
eng1.showdetails()