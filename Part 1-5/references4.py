def play_turn(game_board: list, x: int, y:int, piece:str):

    for row in range(len(game_board)):
        if row==y:
            for column in range(len(game_board[row])):
                if column==x and game_board[row][column]=="":
                    game_board[row][column]=piece
                    return True
    
    return False
        








if __name__ == "__main__":

    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "O"))
    print(play_turn(game_board, 1, 2, "X"))
    print(game_board)