class ShoppingList:
    def __init__(self):
        # Internal storage for products
        self._items = []

    def add(self, product_name: str, quantity: int):
        """
        Add a product and its quantity to the shopping list.
        """
        self._items.append((product_name, quantity))

    def __iter__(self):
        self.n=0

        return self
    
    def __next__(self):
        if self.n < len(self._items):
            item = self._items[self.n]
            self.n+=1

            return item
        else:
            raise StopIteration
        

def products_in_shopping_list(shopping_list: "ShoppingList", amount: int):

    return [item[0] for item  in shopping_list if item[1] >= amount]


if __name__ == "__main__":

    my_list = ShoppingList()
    my_list.add("bananas", 10)
    my_list.add("apples", 5)
    my_list.add("alcohol free beer", 24)
    my_list.add("pineapple", 1)

    print("the shopping list contains at least 8 of the following items:")
    for product in products_in_shopping_list(my_list, 8):
        print(product)