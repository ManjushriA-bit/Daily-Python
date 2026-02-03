class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
         print("Name:", self.name) 
         print("Roll No:", self.roll)

    def result(self):
        if self.marks >= 35:
            print("Pass!!")
        else:
            print("Better luck next time!")
    def grade(self):
        if (self.marks >=85):
            print("Distinction!! ")
        elif(self.marks >= 60):
            print("First Class! ")
        elif(self.marks >=35):
            print("Just Pass")
        else:
            print("Fail ")
        
    def full_report(self):
        self.display()
        self.result()
        self.grade()


s1 = Student("Manju", 1, 62)
s1.display()
s1.result()
s1.grade()
print("------------------------------------")
s2= Student("Krish",163,55)
s2.full_report()