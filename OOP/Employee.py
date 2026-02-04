class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary= salary
    def display(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)
    def bonus(self):
        if (self.salary >= 50000):
            print("Bonus>> 10% ")
        else:
            print("Bonus>> 5% ")

e1=Employee("Krish ",12000)
e1.display()
e1.bonus()

e2=Employee("Krishi ",415000)
e2.display()
e2.bonus()