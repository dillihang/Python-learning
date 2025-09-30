phone_book={}

while True:

    user_input = int(input("Command (1 search, 2 add, 3 quit): "))
    if user_input== 3:
        print("quitting...")
        break

    elif user_input==1:

        searchname = input("Name: ")

        if searchname in phone_book:
            print(phone_book[searchname])

        else:
            print("no number")
             
                



    elif user_input==2:

        name = input("Name: ")
        number = input("Number: ")

        phone_book[name]=number
        print("ok!")

    


                     