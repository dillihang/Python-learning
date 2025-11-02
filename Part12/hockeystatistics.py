import json

class Players:
    """
    Represents a single hockey player with their statistics.

    Attributes:
        name (str): Player's full name.
        nationality (str): Player's nationality code (e.g., CAN, FIN, SWE).
        assists (int): Number of assists scored by the player.
        goals (int): Number of goals scored by the player.
        penalties (int): Number of penalties received by the player.
        team (str): Abbreviation of the team the player belongs to.
        games (int): Number of games played by the player.

    Methods:
        __str__(): Returns a formatted string summarizing the player's stats.
    """
    def __init__(self, name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games

    def __str__(self):
        return f"{self.name:21} {self.team:4} {self.goals:3} + {self.assists} = {self.goals + self.assists:3}"

class PlayersDB:
    """
    Represents a database of hockey players, loaded from a JSON file.

    Attributes:
        player_DB (dict): Dictionary mapping player names to Players objects.

    Methods:
        load_player_objects(file_name): Loads player data from a JSON file and creates Players objects.
        get_player_data(name): Retrieves a Players object by name.
        get_objects(): Returns a list of all Players objects in the database.
    """
    def __init__(self):
        self.player_DB = {}

    def load_player_objects(self, file_name: str):
        with open("part12/" + file_name) as my_file:
            data = my_file.read()
        player_data = json.loads(data)

        for players in player_data:
            self.player_DB[players["name"]]=Players(players["name"], players["nationality"], players["assists"], players["goals"], players["penalties"], players["team"], players["games"])

    def get_player_data(self, name: str):
        if name in self.player_DB:
            return self.player_DB[name]
        
    def get_objects(self,):
        return [self.player_DB[teams] for teams in self.player_DB]

class PlayersApp:
    """
    Main application class for interacting with the hockey players database.

    Provides interactive commands for searching players, listing teams and countries,
    and displaying top players by points or goals.

    Attributes:
        playerapp (PlayersDB): Instance of PlayersDB managing the player data.

    Methods:
        commands(): Prints available user commands.
        search_for_player_by_name(): Prompts for a player name and displays their stats.
        print_teams(): Prints all unique team abbreviations in alphabetical order.
        print_countries(): Prints all unique country abbreviations in alphabetical order.
        print_players_in_team(): Lists players in a selected team sorted by points.
        print_players_from_country(): Lists players from a selected country sorted by points.
        most_points(): Displays top N players by total points, breaking ties by goals.
        most_goals(): Displays top N players by goals, breaking ties by least games played.
        execute(): Starts the interactive application loop.
    """
    def __init__(self):
        self.playerapp=PlayersDB()

    def commands(self):
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def search_for_player_by_name(self):
        player_name = input("name: ")
        player_object = self.playerapp.get_player_data(player_name)
        if player_object is not None:
            print(player_object)
        else:
            print(f"{player_name} does not exist")

    def print_teams(self):
        team_objects = self.playerapp.get_objects()
        teams = list(map(lambda x :x.team, team_objects))
        for team in sorted(set(teams)):
            print(team)

    def print_countries(self):
        team_objects = self.playerapp.get_objects()
        countries = list(map(lambda x:x.nationality, team_objects))
        for country in sorted(set(countries)):
            print(country)

    def print_players_in_team(self):
        team_name = input("team name: ")
        team_objects = self.playerapp.get_objects()
        found = False

        for player_object in sorted(team_objects, key=lambda x:x.goals+x.assists, reverse = True):
            if player_object.team == team_name:
                print(player_object)
                found = True
        
        if not found:
            print(f"No players found for team {team_name}") 

    def print_players_from_country(self):
        country = input("country name: ")
        team_objects = self.playerapp.get_objects()
        found = False

        for player_object in sorted(team_objects, key=lambda x:x.goals+x.assists, reverse = True):
            if player_object.nationality == country:
                print(f"{player_object.name:21} {player_object.nationality:4} {player_object.goals:3} + {player_object.assists} = {player_object.goals + player_object.assists:3}")
                found = True
        
        if not found:
            print(f"No players found for country {country}")   

    def most_points(self):
        how_many = int(input("how many: "))
        team_objects = self.playerapp.get_objects()
        new_size = sorted(team_objects, key = lambda x:(x.goals+x.assists, x.goals), reverse = True)
        try:
            new_size = new_size[0:how_many]
        except (IndexError):
            new_size = new_size[0:]

        for player_objects in new_size:
            print(player_objects)

    def most_goals(self):
        how_many = int(input("how many: "))
        team_objects = self.playerapp.get_objects()
        new_size = sorted(team_objects, key = lambda x:(x.goals, -x.games), reverse = True)
        try:
            new_size = new_size[0:how_many]
        except (IndexError):
            new_size = new_size[0:]

        for player_objects in new_size:
            print(player_objects)

    def execute(self):
        file_name = input("file name: ")
        if file_name == "partial.json":
            self.playerapp.load_player_objects(file_name)
            print(f"read the data of {len(self.playerapp.player_DB)} players")
            self.commands()       
            while True:
                try: 
                    numb = int(input("command: "))
                    if numb == 0:
                        break
                    elif numb == 1:
                        self.search_for_player_by_name()
                    elif numb == 2:
                        self.print_teams()
                    elif numb == 3:
                        self.print_countries()
                    elif numb == 4:
                        self.print_players_in_team()
                    elif numb == 5:
                        self.print_players_from_country()
                    elif numb == 6:
                        self.most_points()
                    elif numb == 7:
                        self.most_goals()
                    else:
                        self.commands()
                except (ValueError):
                    self.commands()

if __name__ == "__main__":

    app = PlayersApp()
    app.execute()