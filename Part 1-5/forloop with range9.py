def all_the_longest(my_list : str):

    long = []

    names = []

    for index in range(len(my_list)):

        long.append(len(my_list[index]))
    # print(long)
    long=max(long)
    # print(long)

    for index in range(len(my_list)):
        if len(my_list[index]) == long:
            names.append(my_list[index])
        
    return names        
        




my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = all_the_longest(my_list)
print(result)

my_list = ["first", "second", "fourth", "eleventh"]

result = all_the_longest(my_list)
print(result)