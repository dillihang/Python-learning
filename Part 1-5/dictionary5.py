phone_book={}

while True:

    user_input = int(input("Command (1 search, 2 add, 3 quit): "))
    if user_input== 3:
        print("quitting...")
        break

    elif user_input==1:

        searchname = input("Name: ")

        if searchname in phone_book:
            for numb in phone_book[searchname]:
                print(numb)

        else:
            print("no number")
             
                



    elif user_input == 2:
        name = input("Name: ")
        number = input("Number: ")

        if name not in phone_book:
            phone_book[name] = []  # create a new list only if name is new

        if number != "":
            phone_book[name].append(number)
            print("ok!")
   




    # elif user_input==2:

    #     name = input("Name: ")

    #     phone_book[name]=[]
        
    #     number = input("Number: ")

        
    #     if number != "" and name in phone_book:
    #         phone_book[name].append(number)
    #     else:
    #         phone_book[name].append(number)

        
    #     print("ok!")

    


                     