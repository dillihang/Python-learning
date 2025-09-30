def length_of_longest(my_list : str):

    highest = []

    for words in my_list:

        highest.append(len(words))
        # print(highest)
    return(max(highest))
    
    


my_list = ["first", "second", "fourth", "eleventh"]

result = length_of_longest(my_list)
print(result)

my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = length_of_longest(my_list)
print(result)



