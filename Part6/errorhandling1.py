def new_person(name: str, age: int):

  
    if name == "":
        raise ValueError("Name is empty: " + name)
        
    elif  len(name.split())<2:
         raise ValueError("name is less than 2 words: " + name)

    elif len(name)>40:
        raise ValueError("The length of name is more than 40 characters long: " + name)

    elif age <0:
        raise ValueError("The age was negative: " + str(age))

    elif age > 150:
        raise ValueError("The age was more than 150: " + str(age))

    else:

        return (name, age)
            
       
            


print(new_person("", 25))
print(new_person("john", 25 ))
print(new_person("john fsdjlfjsd fjsljdf ksdjf skljf skldjfkjfslkdfjsdlkfjslkfjlsdjkfjsdfksddfsdfs", 25 ))
print(new_person("john hardbringer", -50 ))
print(new_person("john hardbringer", 15000 ))
print(new_person("john hardbringer", 25))

