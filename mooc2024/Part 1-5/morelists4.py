
def who_won(game_board: list):

    totalcounter1=[]
    totalcounter2=[]

    for index in game_board:
        counter1=index.count(1)
        counter2=index.count(2)
    totalcounter1.append(counter1)
    totalcounter2.append(counter2)
    # print(sum(totalcounter1))
    # print(sum(totalcounter2))

    if sum(totalcounter1) == sum(totalcounter2):

        return 0

    elif sum(totalcounter1) > sum(totalcounter2):

        return 1
    
    else:
        return 2



if __name__ == "__main__":

    game_board = [
  [1, 0, 0, 0, 2, 0, 1, 0, 0],
  [0, 0, 0, 2, 1, 0, 2, 0, 0],
  [0, 2, 0, 1, 0, 0, 0, 0, 2],
  [0, 1, 2, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 2, 0, 1, 0, 0],
  [2, 0, 1, 0, 2, 0, 2, 0, 0],
  [0, 0, 1, 1, 0, 0, 2, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 1],
  [2, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(who_won(game_board))