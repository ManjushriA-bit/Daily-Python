def factorial(num):
    fact=1
    for i in range (1,num+1):
        fact=fact * i
    
    return fact 
    
fact=factorial(5)
print(fact)
factorial(4)


'''def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return f"{num}! = {fact}"

result = factorial(5)
print(result)
'''