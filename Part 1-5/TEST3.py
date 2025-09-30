gift = int(input("Enter gift: "))

gifttot = 0

if gift>=5000:
    if gift>25000:
        if gift>55000:
            if gift>200000:
                if gift>1000000:
                    gifttot = (142100+(gift-1000000)*0.17)
                else:
                    gifttot = (22100+(gift-200000)*0.15)
            else:
                gifttot = (4700+(gift-55000)*0.12)
        else:
            gifttot = (1700+(gift-25000)*0.10)
    else:
        gifttot = (100+(gift-5000)*0.08)

if gifttot>0:
    print("amount of tax: " + str(int(gifttot)) + " euros")

else:
    print("No Tax!")
   
          
#Nested
