alpha = "A"
num = 1

for i in range(1, 6):      # number of rows
    for j in range(i):

        if num % 2 == 0:   # even number → print alphabet
            print(alpha, end=" ")
            alpha = chr(ord(alpha) + 1)
        else:              # odd number → print number
            print(num, end=" ")

        num += 1

    print()
