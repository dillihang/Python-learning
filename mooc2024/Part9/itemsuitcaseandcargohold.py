import random

class Item:
    """
    This module contains three classes: Item, Suitcase, and CargoHold.

    - Item: represents an item with a name and weight (encapsulated attributes).
    - Suitcase: can hold multiple Items without exceeding a maximum weight.
    - CargoHold: can hold multiple Suitcases without exceeding a maximum weight.
    """
    def __init__(self, name: str, weight: float):
        self.__name = name
        self.__weight = weight

    def weight(self):
        return self.__weight
    
    def name(self):
        return self.__name
    
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
    def __init__(self, max_weight: float):
        self.max_weight = max_weight
        self.all_items = []
        
    def add_item(self, item: "Item"):
        if self.weight() + item.weight() <= self.max_weight:
            self.all_items.append(item)
       
    def print_items(self):

        for items in self.all_items:
            print(items)

    def weight(self):
        total_weight=0
        for items in self.all_items:
            total_weight+=items.weight()

        return total_weight
    
    def heaviest_item(self):
        all_weights=[]
        heavy_items=[]

        if len(self.all_items)==0:
            return None
        else:
            for item in self.all_items:
                all_weights.append(item.weight())
        
            heavy_item_weight = max(all_weights)

            for items in self.all_items:
                if items.weight() == heavy_item_weight:
                    heavy_items.append(items)
            
            return random.choice(heavy_items)

    def __str__(self):
        if len(self.all_items)>1:
            return f"{len(self.all_items)} items ({self.weight()} kg)"
        else:
            return f"{len(self.all_items)} item ({self.weight()} kg)"

class CargoHold:
    def __init__(self, max_weight: float):
        self.max_weight = max_weight
        self.all_suitcases = []

    
    def add_suitcase(self, suitcase : "Suitcase"):
        new_max_weight=0
        
        for items in self.all_suitcases:
            new_max_weight+=items.weight()

        if suitcase.weight()<self.max_weight-new_max_weight:
            self.all_suitcases.append(suitcase)
        else:
            pass

    def print_items(self):
        for suitcase in self.all_suitcases:
            for items in suitcase.all_items:
                print (items)
            
    def __str__(self):
        new_max_weight=0
        for items in self.all_suitcases:
            new_max_weight+=items.weight()

        if len(self.all_suitcases)>1:
            return f"{len(self.all_suitcases)} suitcases, space for {self.max_weight-new_max_weight} kg"
        else:
            return f"{len(self.all_suitcases)} suitcase, space for {self.max_weight-new_max_weight} kg"

if __name__=="__main__":
    
    cargo_hold = CargoHold(1000)
    print(cargo_hold)

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold.add_suitcase(adas_suitcase)
    print(cargo_hold)

    cargo_hold.add_suitcase(peters_suitcase)
    print(cargo_hold)