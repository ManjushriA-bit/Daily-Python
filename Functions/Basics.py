"""
#Addition function
def add(a, b):
    return a + b

result = add(10, 30)
print(result)
"""

"""
#Even Odd Function
def even_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False

result = even_odd(230)
print(result)
"""

"""

#Write a function that takes 3 numbers and returns the largest number.

def largestNo(a,b,c):
    return max(a,b,c)

Large= largestNo(9,192,202)
print(Large)
"""

#Factorial using loops and functions 

def Factorial(num):
    fact=1
    for i in range(1,num+1):
        fact= fact*i
    return fact

Fact= Factorial(5)
print(Fact)