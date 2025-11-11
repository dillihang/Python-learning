mylist = [1,2,3,4,5]

while True:

    indx = int(input("Please enter the index: "))
    
    if indx == -1:
        break

    new_value = int(input("please enter new value: "))

    
    mylist[indx] = new_value

    print(mylist)