def get_details(name:str, age:int, height:float):

    persontup=()

    persontup = name, age, height

    return persontup



def store_personal_data(person: tuple):
     


     with open("Part 6/people.csv", "a") as file:


        
        file.write(f"{person[0]};{person[1]};{person[2]}\n")
    




person=get_details("Paul Paulson", 37, 175.5)

store_personal_data(person)