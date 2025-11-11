def transpose(matrix: list):

    newmatrix=[]
    
    for rows in range(len(matrix)):
        for cols in range(len(matrix[rows])):

            if len(newmatrix)<=cols:
                newmatrix.append([])

            newmatrix[cols].append(matrix[rows][cols])



    for rows in newmatrix:
        print(rows)
            




if __name__ == "__main__":

    matrix = [
    [1 ,2 ,3],
    [4 ,5, 6],
    [7 ,8 ,9],
    ]


transpose(matrix)