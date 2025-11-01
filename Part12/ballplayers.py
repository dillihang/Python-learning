class BallPlayer:
    def __init__(self, name: str, shirt_number: int, scored_goals: int, assists: int, minutes: int):
        self.name = name
        self.shirt_number = shirt_number
        self.scored_goals = scored_goals
        self.assists = assists
        self.minutes = minutes
    
    def __str__(self):
        return f"BallPlayer(name={self.name}, number={self.shirt_number}, goals={self.scored_goals}, passes={self.assists}, minutes={self.minutes})"

def most_goals(players_list: list):
    player=max(players_list, key=lambda player: player.scored_goals)
    return(player.name)

def most_points(players_list: list):
    player=max(players_list, key=lambda player: player.scored_goals + player.assists)
    return(player.name, player.shirt_number)

def least_minutes(players_list: list):
    return min(players_list, key=lambda player: player.minutes)
  
     
if __name__ == "__main__":
    player1 = BallPlayer("Archie Bonkers", 13, 5, 12, 46)
    player2 = BallPlayer("Speedy Tickets", 7, 2, 26, 55)
    player3 = BallPlayer("Cruella De Hill", 9, 1, 32, 26)
    player4 = BallPlayer("Devilled Tasmanian", 12, 1, 11, 41)
    player5 = BallPlayer("Donald Quack", 4, 3, 9, 12)
    
    team = [player1, player2, player3, player4, player5]
    print(most_goals(team))
    print(most_points(team))
    print(least_minutes(team))

    

  