'''
print("Hello World!! ")
a= 10
b=12
sum= a+b
print(f"Sum> {sum}")

a=int(input("Enter the first number: "))
b=int(input("Enter the Second number: "))
print(f"Sum of {a} and {b} is: {a+b}")
'''
def add(x, y=2):
    return x + y

print(add(3))
print(add(3, 5))