with open("Part 6/diary.txt") as file:
            print("Entries:")
            for line in file:
                
                if line != "":
                   
                    print(line.strip())
                   
                else:
                    print("Diary is empty")


while True:

    print("1 - add an entry, 2 - read entries, 0 - quit")
    number=int(input("Function: "))
    
    if number==0:
        print("Bye now!")
        break

    
    elif number==2:
        
        with open("Part 6/diary.txt") as file:
            print("Entries:")
            for line in file:
                if line=="":
                     continue
                else:
                    
                    print(line.strip())
                    

    elif number==1:
        entry=input("Diary entry: ")

        with open("Part 6/diary.txt", "a") as my_file:

            my_file.write(f"{entry}\n")
            print("Diary saved")