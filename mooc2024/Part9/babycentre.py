class Person:
    """
    This program models persons and a BabyCentre that can weigh and feed them.

    Classes:
    - Person: stores a person's name, age, height, and weight.
    - BabyCentre: performs actions on Person objects.
    • weigh(person): returns the person's weight and counts the weigh-in.
    • feed(person): increases the person's weight by 1.
    • weigh_ins(): returns the total number of weigh-ins performed.

    Example usage:
    Create Person objects, feed them, weigh them, and track the number of weigh-ins.
    """

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return str(self.__dict__)
    
    def __repr__(self):
        return str(self.__dict__)
    
class BabyCentre:

    def __init__(self):
        self.noofweighins=0
      

    def weigh(self, person: Person):
        
        self.noofweighins+=1
        return person.weight
    
    def feed(self, person: Person):
        person.weight+=1

    def weigh_ins(self):

        return self.noofweighins
    
    
if __name__=="__main__":

    baby_centre = BabyCentre()

    eric = Person("Eric", 1, 110, 7)
    peter = Person("Peter", 33, 176, 85)

    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

    baby_centre.weigh(eric)
    baby_centre.weigh(eric)

    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

    baby_centre.weigh(eric)
    baby_centre.weigh(eric)
    baby_centre.weigh(eric)
    baby_centre.weigh(eric)

    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")