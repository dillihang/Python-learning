class SuperHero:
   def __init__(self, name: str, powers: str):
      self.name = name
      self.powers = powers

class SuperGroup():
   def __init__(self, name: str, location: str):
      self._name = name
      self._location = location
      self._members = []

   @property
   def name(self):
      return self._name
   
   @property
   def location(self):
      return self._location
   
   def add_member(self, hero: "SuperHero"):
      self._members.append(hero)
   
   def print_group(self):
      print(f"{self.name}, {self.location}")
      print(f"Members: ")
      for superheros in self._members:
         print(f"{superheros.name}, superpowers: {superheros.powers}") 


if __name__ == "__main__":
   superperson = SuperHero("SuperPerson", "Superspeed, superstrength")
   invisible = SuperHero("Invisible Inca", "Invisibility")
   revengers = SuperGroup("Revengers", "Emerald City")

   revengers.add_member(superperson)
   revengers.add_member(invisible)
   revengers.print_group()
   # name = revengers.get_name
   # revengers.get_location
   # print(name)