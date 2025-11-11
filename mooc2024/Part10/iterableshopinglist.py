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


if __name__ == "__main__":
    shopping_list = ShoppingList()
    shopping_list.add("bananas", 10)
    shopping_list.add("apples", 5)
    shopping_list.add("pineapple", 1)

    for product in shopping_list:
        print(f"{product[0]}: {product[1]} units")