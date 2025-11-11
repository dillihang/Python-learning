def length(my_list : list):

    return len(my_list)

def mean(my_list : list):

    return sum(my_list)/len(my_list)


def range_of_list(my_list : list):

    return max(my_list) - min(my_list)



my_list = [1, 2, 3, 4, 5]
result = length(my_list)
print("The length is", result)

# the list given as an argument doesn't need to be stored in any variable
result = length([1, 1, 1, 1])
print("The length is", result)

my_list = [1, 2, 3, 4, 5]
result = mean(my_list)
print("mean value is", result)

my_list = [1, 2, 3, 4, 5]
result = range_of_list(my_list)
print("The range of the list is", result)