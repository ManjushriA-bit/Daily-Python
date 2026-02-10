password="Py@123"
trials=1
while trials<=3:
    pin=input(f"Trial -{trials} | pin>> ")
    trials+=1
    if pin==password:
        print("Sucessfull !! ")
        break
    else:
        print("Try again ")