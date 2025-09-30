attempts=0

while True:

    pin = int(input("please enter your pin: "))
    attempts +=1
    success = attempts ==1
    if pin == 4321:
        if success:
            print("Correct! It only took you one single attempt!")
            break
            
        print("Correct it took you " + str(attempts) + " attempts!")
        break

    print("wrong")

