def count_matching_elements(my_matrix: list, element : int):

    counter=0

    for rows in my_matrix:
        print(f"Rows")
        print(rows)
        for numb in rows:
            if element == numb:
                counter+=1

    return counter








if __name__ == "__main__":

    my_matrix = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(my_matrix, 1))