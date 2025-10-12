def number_in_list(numbers: list, searched_number: int):
    for number in numbers:
        if number == searched_number:
            return True

    return False
        

found = number_in_list([1, 2, 3, 4], 5)
print(found)  # prints out False


