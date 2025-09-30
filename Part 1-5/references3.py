def print_sudoku(sudoku: list):
    
    """This functions converts the sudoku into "_" if the index value is 0 and if the index value is higher than 0, which is its own value
    is then added to the boardstr(str) as a string."""

    boardstr=""

    for rows in range(len(sudoku)):
        for columns in range(len(sudoku[rows])):

            if sudoku[rows][columns] == 0:
                boardstr+="_"
            elif sudoku[rows][columns]>0:
                boardstr+=str(sudoku[rows][columns])

   
    i=1
    j=0
    while i<9:
        while j<len(boardstr):


            print(f"{boardstr[j]} {boardstr[j+1]} {boardstr[j+2]}   {boardstr[j+3]} {boardstr[j+4]} {boardstr[j+5]}  {boardstr[j+6]} {boardstr[j+7]} {boardstr[j+8]}")

            if i==3:
                print()
            elif i==6:
                print()

            i+=1
            j+=9

 

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):

    """This functions basically locates the row and column that was input and replaces the value of that index to a new number. it 
    does not create new sudoku list but rather changes the current sudoku list and returns it for the print_sudoku function to display"""

    grid_copy=[]

    for row in sudoku:
        newrow=[]
        for value in row:
            newrow.append(value)
        grid_copy.append(newrow)



    # print(grid_copy)

    for row in range(len(sudoku)):
        if row==row_no:

            for columns in range(len(sudoku[row_no])):
                if columns == column_no:
                    grid_copy[row][columns]=number
                    # print(columns)

    
    return grid_copy
    

if __name__ == "__main__":
    
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]


    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)