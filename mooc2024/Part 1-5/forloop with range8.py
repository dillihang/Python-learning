def shortest(my_list : str):
    
    names = []
    short = []

    for index in range(len(my_list)):

        short.append(len(my_list[index]))
    # print(short)
    short=min(short)
    # print(short)

    for index in range(len(my_list)):
        if len(my_list[index]) == short:
            names.append(my_list[index])


    return names
        
        




my_list = ["adele", "mark", "dorothy", "tim", "bob", "hedy", "richard"]

result = shortest(my_list)
print(result)

my_list = ["first", "second", "fourth", "eleventh"]

result = shortest(my_list)
print(result)