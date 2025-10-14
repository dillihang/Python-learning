class Person:
    """
    This module defines classes for a Room and Persons.
    You can add people to the room, check the shortest person,
    remove the shortest person, and print the room contents.
    """
    def __init__(self, name: str, height: float):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name
    
class Room:
    def __init__(self):
        self.list_of_person = []
        self.totalheight = 0

    def add(self, person: "Person"):
    
        self.list_of_person.append(person)
        self.totalheight+=person.height

    def is_empty(self):
        return len(self.list_of_person) == 0
        
    def print_contents(self):
        print(f"There are {len(self.list_of_person)} persons in the room, and their combined height is {self.totalheight} cm")
        for person in self.list_of_person:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if len(self.list_of_person) == 0:
            return None
        else:
            shortest_person = self.list_of_person[0]  
            for person in self.list_of_person:
                if person.height < shortest_person.height:
                    shortest_person = person
            return shortest_person
        
    def remove_shortest(self):
        if len(self.list_of_person) == 0:
            return None
        else:
            position = self.list_of_person.index(self.shortest())
            removedperson = self.list_of_person.pop(position)
            return removedperson
        
    
     
if __name__=="__main__":

    # room = Room()

    # print("Is the room empty?", room.is_empty())
    # print("Shortest:", room.shortest())

    # room.add(Person("Lea", 183))
    # room.add(Person("Kenya", 172))
    # room.add(Person("Nina", 162))
    # room.add(Person("Ally", 166))

    # print()

    # print("Is the room empty?", room.is_empty())
    # print("Shortest:", room.shortest())

    # print()

    # room.print_contents()
    
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
        
