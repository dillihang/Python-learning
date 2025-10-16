class ComputerGame:
   """Represents a computer game with a name, developer, and release year."""
   def __init__(self, name: str, developer: str, year: int):
        self.name = name
        self.developer = developer
        self.year = year

class GameWarehouse:
   """Stores a collection of ComputerGame objects."""
   def __init__(self):
      self.games = []

   def add_game(self, game: "ComputerGame"):
      self.games.append(game)

   def list_games(self):
      return self.games
   
class GameMuseum(GameWarehouse):
   """A museum of games that only lists games released before 1990."""
   def __init__(self):
      super().__init__()

   def list_games(self):
      games_1990=[]
      for items in self.games:
         if items.year < 1990:
            games_1990.append(items)

      return games_1990


if __name__ == "__main__":

   museum = GameMuseum()
   museum.add_game(ComputerGame("Pacman", "Namco", 1980))
   museum.add_game(ComputerGame("GTA 2", "Rockstar", 1999))
   museum.add_game(ComputerGame("Bubble Bobble", "Taito", 1986))
   
   # for games in GameWarehouse.list_games():
   #    print(games.name)

   for game in museum.list_games():
      print(game.name)