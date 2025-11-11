
def row_correct(sudoku: list, row_no: int):

    find=[1,2,3,4,5,6,7,8,9]
    counter=[]

    for index in range(len(sudoku)):
        if row_no==index:
            for numbs in sudoku[index]:
                if numbs in find:
                    counter.append(sudoku[index].count(numbs))
    
    # print(counter)

    for count in counter:
        if count>1:
            return False
 
    return True
                        

def Column_correct(sudoku: list, column_no: int):

    find=[1,2,3,4,5,6,7,8,9]
    columnlist=[]
    counter=[]

    for index in range(len(sudoku)):
        
        for column in range(len(sudoku[index])):
            if column==column_no:
                columnlist.append(sudoku[index][column])

    # print(columnlist)
    for numbs in columnlist:
        if numbs in find:
            counter.append(columnlist.count(numbs))
    
    # print(counter)

    for count in counter:
        if count>1:
            return False
        
    return True
            
    
def block_correct(sudoku: list, row_no: int, column_no: int):
    find=[1,2,3,4,5,6,7,8,9]
    newrow=sudoku[row_no:row_no+3]
    newboard=[]
    counter=[]
    # print(newrow)

    for rows in range(len(newrow)):
        # print(newrow[rows])
        for columns in range(column_no, len(newrow[rows])):
            if columns<column_no+3:
                newboard.append(newrow[rows][columns])
    
    print(newboard)

    for numbs in newboard:
        if numbs in find:
            counter.append(newboard.count(numbs))
    print(counter)
    

    for count in counter:
        if count>1:
            return False
        
    return True




if __name__ == "__main__":

    sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

# print(row_correct(sudoku, 0))
# print(row_correct(sudoku, 1))


# print()
# print()
# print()

# print(Column_correct(sudoku, 0))
# print(Column_correct(sudoku, 1))


# print()
# print()
# print()


print(block_correct(sudoku, 0, 0))
print(block_correct(sudoku, 0, 3))
print(block_correct(sudoku, 0, 6))
print(block_correct(sudoku, 3, 0))
print(block_correct(sudoku, 3, 3))
print(block_correct(sudoku, 3, 6))
print(block_correct(sudoku, 6, 0))
print(block_correct(sudoku, 6, 3))
print(block_correct(sudoku, 6, 6))

