
def sum_of_row(my_matrix, row_no: int):
    # choose the desired row from within the matrix
    row = my_matrix[row_no]
    row_sum = 0
    for item in row:
        row_sum += item

    return row_sum



def sum_of_column(my_matrix, column_no: int):
    # go through each row and select the item at the chosen position
    column_sum = 0
    for row in my_matrix:
        column_sum += row[column_no]

    return column_sum


def change_value(my_matrix, row_no: int, column_no: int, new_value: int):
    # choose the desired row
    row = my_matrix[row_no]
    # select the correct item within the row
    row[column_no] = new_value



matrix = [[1,2,3], [4,5,6], [7,8,9]]

for i in range(len(matrix)): # using the number of rows in the matrix
    for j in range(len(matrix[i])): # using the number of items on each row 
        matrix[i][j] += 1

print(matrix)


if __name__ == "__main__":

    m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]

    my_sum = sum_of_row(m, 0)
    print(my_sum) # prints out 33 (which equals 9 + 1 + 12 + 11)

    my_sum = sum_of_column(m, 2)
    print(my_sum) # prints out 39 (which equals 3 + 12 + 9 + 15)

    m1 = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]

    print(m1)
    change_value(m1, 2, 3, 1000)
    print(m1)