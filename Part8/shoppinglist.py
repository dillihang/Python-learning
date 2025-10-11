class ShoppingList:
    def __init__(self):
        self.items = []
        self.amounts = []

    def add(self, name, quantity):
        self.items.append(name)
        self.amounts.append(quantity)

    def number_of_items(self):
        return len(self.items)

    def item(self, i):
        return self.items[i-1]  # 1-indexed

    def amount(self, i):
        return self.amounts[i-1]  # 1-indexed



def total_units(my_list: ShoppingList):

    return sum(my_list.amounts)

if __name__ == "__main__":
    my_list = ShoppingList()
    my_list.add("bananas", 10)
    my_list.add("apples", 5)
    my_list.add("pineapple", 1)

    print(total_units(my_list))  # Output: 16
