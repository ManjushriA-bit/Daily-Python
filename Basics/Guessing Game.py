import random

RanNum = random.randint(1, 100)

for i in range(5):
    num = int(input(f"Trial {i+1}: Guess the number (1-100): "))

    if num == RanNum:
        print("You nailed it!! 🎯")
        print(f"The number is {RanNum}")
        break
    elif num > RanNum:
        print("Too High!! 🔼")
    else:
        print("Too Low!! 🔽")
else:
    print(f"Out of trials! The number was {RanNum}")
