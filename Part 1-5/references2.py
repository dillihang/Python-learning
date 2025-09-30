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

 

def add_number(sudoku: list, row_no: int, column_no: int, number: int):

    """This functions basically locates the row and column that was input and replaces the value of that index to a new number. it 
    does not create new sudoku list but rather changes the current sudoku list and returns it for the print_sudoku function to display"""
     
    for row in range(len(sudoku)):

        if row==row_no:

            for columns in range(len(sudoku[row_no])):
                if columns == column_no:
                    sudoku[row][columns]=number
                    # print(columns)

    return sudoku
    
    

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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)