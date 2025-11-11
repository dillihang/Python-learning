class Present:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight} kg)"
    
class Box:
    def __init__(self):
        self.presents = []
        self.total_weight_value = 0
   
    def add_present(self, present: "Present"):
        self.presents.append(present)
        self.total_weight_value += present.weight

    def total_weight(self):
        return self.total_weight_value


if __name__=="__main__":
    
    book = Present("ABC Book", 2)

    box = Box()
    box.add_present(book)
    print(box.total_weight())

    cd = Present("Pink Floyd: Dark Side of the Moon", 1)
    box.add_present(cd)
    print(box.total_weight())
        
        
