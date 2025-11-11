"""
This program models a cafeteria payment system with two main components:

Classes:
- LunchCard: keeps track of a card's balance and allows deposits or subtractions.
  • deposit_money(amount): adds money to the card.
  • subtract_from_balance(amount): reduces the balance if enough funds are available; returns True if successful, False otherwise.

- PaymentTerminal: simulates a cafeteria terminal handling cash and card payments.
  • eat_lunch(payment): processes a regular lunch payment in cash; returns change if payment is enough.
  • eat_special(payment): processes a special lunch payment in cash; returns change if payment is enough.
  • eat_lunch_lunchcard(card): charges a regular lunch to a LunchCard if balance is sufficient.
  • eat_special_lunchcard(card): charges a special lunch to a LunchCard if balance is sufficient.
  • deposit_money_on_card(card, amount): deposits cash onto a LunchCard and increases terminal funds.

The system keeps track of funds available at the terminal and the number of lunches sold.
"""
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):

        if self.balance-amount<0:
            return False
        else:
            self.balance=self.balance-amount
            return True
        
class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        price=2.50
        if payment < price:
            return payment
        else:
            self.lunches+=1
            self.funds+=price
            change = payment - price
            return change


    def eat_special(self, payment: float):
        price=4.30
        if payment < price:
            return payment
        else:
            self.specials+=1
            self.funds+=price
            change = payment - price
            return change

    def eat_lunch_lunchcard(self, card: LunchCard):
        price=2.50
        if card.balance-price<0:
            return False
        else:
            self.lunches+=1
            card.balance= card.balance-price
            return True


    def eat_special_lunchcard(self, card: LunchCard):
        price=4.30
        if card.balance-price<0:
            return False
        else:
            self.specials+=1
            card.balance= card.balance-price
            return True
        
    def deposit_money_on_card(self, card: LunchCard, amount: float):

        if amount<0:
            pass
        else:
            self.funds+=amount
            card.balance=card.balance+amount

        
if __name__ == "__main__":
    
    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)