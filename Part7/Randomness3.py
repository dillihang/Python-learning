import random

dice = {
    "A": (3, 3, 3, 3, 3, 6),
    "B": (2, 2, 2, 5, 5, 5),
    "C": (1, 4, 4, 4, 4, 4)
}

def roll(die: str):
    """Return a random roll of the specified die (A, B, or C)."""

    return random.choice(dice[die])


def play(die1: str, die2: str, times: int):
    """Simulate dice games and return wins/ties."""

    draw=0
    die1_win=0
    die2_win=0

    for _ in range(times):

        roll_Score1=roll(die1)
        roll_Score2=roll(die2)

        if roll_Score1==roll_Score2:
            draw+=1
        
        elif roll_Score1>roll_Score2:
            die1_win+=1
        
        else:
            die2_win+=1
    
    result=(die1_win, die2_win, draw)

    return result


if __name__=="__main__":

    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)
   
    