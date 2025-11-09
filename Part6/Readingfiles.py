def largest():
    with open("Part 6/numbers.txt") as file:
        new_numbers=[]
        for numb in file:
            numb=numb.replace("\n","")
    
            new_numbers.append(int(numb))

    print(max(new_numbers))

largest()

