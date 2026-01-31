def marriage(boy="krish",girl="Krishi"):
    print(f"{boy} Married {girl} !! ")

marriage()
marriage("Ram")
marriage("Sita", "Ram")
''' 
marriage(boy="Ram", girl="Sita")
# SyntaxError: positional argument follows keyword argument
'''
marriage(boy="Ram", girl="Sita ")