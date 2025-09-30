def chessboard(length):

    i=0
    t=0

    square=0
    
    while t<length:

        board=""
                       
        while i<length:
        
            if square%2!=0:
                board+="0"
            else:
                board+="1"
            
            square+=1

            i+=1
        print(board)
        i=0
        t+=1

        if length%2==0:
            square+=1




chessboard(3)
