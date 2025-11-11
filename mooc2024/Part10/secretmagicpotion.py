class MagicPotion:
    """A basic magic potion with a name and a list of ingredients."""
    def __init__(self, name: str):
        self.name = name
        self.ingredient_list = []

    def add_ingredient(self, ingredient: str, amount: float):
        self.ingredient_list.append((ingredient, amount))

    
    def print_recipe(self):
        print(f"{self.name}:")
        for items in self.ingredient_list:
            print(f"{items[0]} {items[1]} grams")


class SecretMagicPotion(MagicPotion):
    """A MagicPotion with password-protected access to adding ingredients and printing the recipe."""
    def __init__(self, name: str, actual_password: str):
        super().__init__(name)
        self._actual_password = actual_password
    
    def add_ingredient(self, ingredient, amount, password: str):
        if password == self._actual_password:
            super().add_ingredient(ingredient, amount)
        else:
            raise ValueError("Wrong password!")
    
    def print_recipe(self, password: str):
        if password == self._actual_password:
            super().print_recipe()
        else:
            raise ValueError("Wrong password!")


if __name__ == "__main__":
    diminuendo = SecretMagicPotion("Diminuendo maximus", "hocuspocus")
    diminuendo.add_ingredient("Toadstool", 1.5, "hocuspocus")
    diminuendo.add_ingredient("Magic sand", 3.0, "hocuspocus")
    diminuendo.add_ingredient("Frogspawn", 4.0, "hocuspocus")
    diminuendo.print_recipe("hocuspocus")

    diminuendo.print_recipe("pocushocus") # WRONG password!

    # dimuiendo = MagicPotion("Diminuewndo maximus")
    # dimuiendo.add_ingredient("Toadstool", 1.5)
    # dimuiendo.add_ingredient("Magic sand", 3.0)
    # dimuiendo.print_recipe()