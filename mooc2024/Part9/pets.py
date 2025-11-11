class Pet:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed
        
class Person:
    def __init__(self, name: str, pet: "Pet"):
        self.pet = pet
        self.name = name
    
    def __str__(self):
        return f"{self.name}, Whose pal is {self.pet.name}, a {self.pet.breed}"         


if __name__ == "__main__":

    hulda = Pet("Hulda", "mixed-breed dog")
    levi = Person("Levi", hulda)

    print(levi)


        
        