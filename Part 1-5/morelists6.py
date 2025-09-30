def row_correct(sudoku: list, row_no: int):

    """ Checks the rows in the baord. The function should return True or False, depending on whether the row is 
    filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once  """

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
                        

def column_correct(sudoku: list, column_no: int):

    
    """ Checks the column in the baord. The function should return True or False, depending on whether the column is 
    filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once  """

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

    
    """ Checks the blocks in the baord. The function should return True or False depending on whether the 3 by 3 block 
    to the right and down from the given indexes is filled in correctly. That is, whether the block contains each of 
    the numbers 1 to 9 at most once.  """

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
    
    # print(newboard)

    for numbs in newboard:
        if numbs in find:
            counter.append(newboard.count(numbs))
    # print(counter)
    

    for count in counter:
        if count>1:
            return False
        
    return True




def sudoku_grid_correct(sudoku: list):

    """final check. The function should check each of the nine rows, columns and 3 by 3 blocks in the grid. If all contain each of the numbers
    1 to 9 at most once, the function returns True. If a single one is filled in incorrectly, the function returns False."""

    finallist = []

    index=0
    while index < 9:
        finallist.append(str(row_correct(sudoku, index)))
        finallist.append(str(column_correct(sudoku, index)))

        index+=1 

    i=0
    t=0

    while i <= 6:

        while t <= 6:
            finallist.append(str(block_correct(sudoku, i, t)))
            t+=3
        t=0
        i+=3

    # print(finallist)

    for boolvalue in finallist:
        if boolvalue == "False":
            return False
    
    return True
    

            


if __name__ == "__main__":

    sudoku1 = [
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


print(sudoku_grid_correct(sudoku1))


sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
]

print(sudoku_grid_correct(sudoku2))