class BankAccount:
    """
    BankAccount class models a simple bank account with private attributes for owner name,
    account number, and balance. 

    It provides methods to deposit and withdraw money. Each operation automatically applies
    a 1% service charge using a private method. The balance can be accessed via a getter
    property, but cannot be modified directly from outside the class.
    """


    def __init__(self, name: str, account_no: str, balance: float):
        self.__name = name
        self.__account_no = account_no
        self.__balance = balance
    
    def deposit(self, amount: float):
        if amount<0:
            raise ValueError("Amount needs to be non-negative")
        else:
            self.__balance += amount
            self.__service_charge()

    def withdraw(self, amount: float):
        if self.__balance-amount <0:
            raise ValueError("not enough money")
        else:
            self.__balance -= amount
            self.__service_charge()

    @property
    def balance(self):
        return self.__balance

    def __service_charge(self):
        charge_value = self.__balance * 0.01
        self.__balance = self.__balance - charge_value

        
   
if __name__=="__main__":

    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)
