mylist = []

print(f"The list is now {mylist}")

items=1

while True:
    
    user_input = input(f"a(d)d, (r)emove or e(x)it: ")
    if user_input == "x":
        print("Bye!")
        break
        

    if user_input == "d":

        mylist.append(items)

        items += 1
        print(items)
        
        print(f"The list is now {mylist}")

    if user_input == "r":

        print(items)

        mylist.remove(items-1)
        

        items -=1
        print(items)

        print(f"The list is now {mylist}")


