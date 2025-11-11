def all_the_longest(my_list : str):

    longestnames = []

    long_name = len(my_list[0])
    longest = my_list[0]

    for names in my_list:

        if len(names)>long_name:
            longest=names
            # print(longest)
    longestnames.append(longest)
    print(longestnames)



my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = all_the_longest(my_list)
print(result)

my_list = ["first", "second", "fourth", "eleventh"]

result = all_the_longest(my_list)
print(result)