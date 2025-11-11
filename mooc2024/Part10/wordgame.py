import random

class WordGame():
   """Base class for a two-player word game.

   Attributes:
      wins1 (int): Number of rounds won by player 1.
      wins2 (int): Number of rounds won by player 2.
      rounds (int): Total number of rounds to play.

   Methods:
      round_winner(player1_word, player2_word):
         Determines the winner of a round. Random by default.
      play():
         Plays the game for the given number of rounds.
   """
   def __init__(self, rounds: int):
      self.wins1 = 0
      self.wins2 = 0
      self.rounds = rounds

   def round_winner(self, player1_word: str, player2_word: str):
      # determine a random winner
      return random.randint(1, 2)

   def play(self):
      print("Word game:")
      for i in range(1, self.rounds+1):
         print(f"round {i}")
         answer1 = input("player1: ")
         answer2 = input("player2: ")

         if self.round_winner(answer1, answer2) == 1:
            self.wins1 += 1
            print("player 1 won")
         elif self.round_winner(answer1, answer2) == 2:
            self.wins2 += 1
            print("player 2 won")
         else:
            pass # it's a tie

      print("game over, wins:")
      print(f"player 1: {self.wins1}")
      print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
   """Word game where the player with the longest word wins each round."""
   def __init__(self, rounds: int):
      super().__init__(rounds)

   def round_winner(self, player1_word: str, player2_word: str):
            
      if len(player1_word)>len(player2_word):
         return 1
      elif len(player1_word)<len(player2_word):
         return 2
      else:
         return 0
      
class MostVowels(WordGame):
   """Word game where the player with the most vowels in their word wins each round."""
   def __init__(self, rounds):
      super().__init__(rounds)
   
   def round_winner(self, player1_word, player2_word):
      vowels = "aeiou"
      player1_count=0
      player2_count=0

      for char in player1_word.lower():
         if char in vowels:
            player1_count+=1
      
      for char in player2_word.lower():
         if char in vowels:
            player2_count+=1
      
      if player1_count>player2_count:
         return 1
      elif player1_count<player2_count:
         return 2
      else:
         return 0
      
class RockPaperScissors(WordGame):
   """Classic rock-paper-scissors game.

   Rules:
      - Rock beats scissors
      - Paper beats rock
      - Scissors beats paper
      - Invalid input loses the round
      - Tie if both inputs are the same or both invalid
   """
   def __init__(self, rounds):
      super().__init__(rounds)
   
   def round_winner(self, player1_word, player2_word):
      rps ={"rock", "paper", "scissors"}

      if player1_word not in rps and player2_word not in rps:
         return 0
      elif player1_word not in rps:
         return 2
      elif player2_word not in rps:
         return 1
     
      if player1_word==player2_word:
         return 0
      elif player1_word == "rock" and player2_word == "scissors" \
         or player1_word == "paper" and player2_word == "rock" \
         or player1_word == "scissors" and player2_word == "paper":
         return 1
      else:
         return 2

   # def round_winner(self, player1_word, player2_word):
   #    rps_dict ={"rock": 1, "paper": 2, "scissors": 3}

   #    if player1_word not in rps_dict and player2_word not in rps_dict:
   #       return 0
   #    elif player1_word not in rps_dict:
   #       return 2
   #    elif player2_word not in rps_dict:
   #       return 1
      
   #    result = (rps_dict[player1_word] - rps_dict[player2_word]) % 3
   #    if result == 0:
   #       return 0
   #    elif result == 1:
   #       return 1
   #    else:
   #       return 2

if __name__ == "__main__":

   p = RockPaperScissors(4)
   p.play()