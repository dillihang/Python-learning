class LunchCard:
    """
    This program defines a LunchCard class that simulates a cafeteria debit card system.

    Features:
    - Each LunchCard instance has a balance (in euros).
    - The cardholder can:
    • eat_lunch(): deducts 2.60 euros if sufficient funds are available
    • eat_special(): deducts 4.60 euros if sufficient funds are available
    • deposit_money(amount): adds the given amount to the balance
        - Raises ValueError if the deposit amount is negative
    - The __str__ method returns the balance formatted to one decimal place.

    The main program demonstrates the following scenario:
    - Peter and Grace each start with a card balance
    - They buy lunches and specials
    - Peter makes a deposit and eats again
    - Grace also makes a deposit
    - Their updated balances are printed after each stage
    """
    def __init__(self, balance: float):
        self.balance = balance
    
    def eat_lunch(self):

        if self.balance-2.60<0:
            pass
        else:
            self.balance=self.balance-2.60

    def eat_special(self):

        if self.balance-4.60<0:
            pass
        else:
            self.balance=self.balance-4.60
    
    def deposit_money(self, amount: int):

        if amount<0:
            raise ValueError("You cannot deposit an amount of money less than zero")

        else:
            self.balance=self.balance+amount

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"


if __name__=="__main__":

    Peter = LunchCard(20)
    Grace = LunchCard(30)
    Peter.eat_special()
    Grace.eat_lunch()
    print(f"Peter:{Peter}")
    print(f"Grace:{Grace}")
    Peter.deposit_money(20)
    Grace.eat_special()
    print(f"Peter:{Peter}")
    print(f"Grace:{Grace}")
    Peter.eat_lunch()
    Peter.eat_lunch()
    Grace.deposit_money(50)
    print(f"Peter:{Peter}")
    print(f"Grace:{Grace}")




    