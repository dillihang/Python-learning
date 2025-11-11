class Money:
    """
    A class representing a monetary amount in euros and cents.

    Attributes:
        __tens (int): The euro portion of the amount (private).
        __hundreds (int): The cents portion of the amount (private).

    Methods:
        __str__(): Returns a formatted string representation, e.g., "4.05 eur".
        __eq__(other): Checks if two Money objects are equal.
        __ne__(other): Checks if two Money objects are not equal.
        __gt__(other): Checks if this Money object is greater than another.
        __lt__(other): Checks if this Money object is less than another.
        __add__(other): Returns a new Money object representing the sum.
        __sub__(other): Returns a new Money object representing the difference,
                        raises ValueError if the result would be negative.

    Notes:
        - All attributes are private; direct access or modification is not allowed.
        - Addition and subtraction return new Money instances; original objects are unchanged.
    """
    def __init__(self, tens: int, hundreds: int):
        self.__tens = tens
        self.__hundreds = hundreds
    
    def __str__(self):
        return f"{self.__tens}.{self.__hundreds:02d} eur"       
   
    def __eq__(self, another):
        return self.__tens + self.__hundreds/100 == another.__tens + another.__hundreds/100 
    
    def __gt__(self, another):
        return self.__tens + self.__hundreds/100 > another.__tens + another.__hundreds/100

    def __lt__(self, another):
        return self.__tens + self.__hundreds/100 < another.__tens + another.__hundreds/100
    
    def __ne__(self, another):
        return self.__tens + self.__hundreds/100 != another.__tens + another.__hundreds/100
    
    def __add__(self, another):

        result1 = self.__tens + self.__hundreds/100 
        result2 = another.__tens + another.__hundreds/100
        final_result = result1 + result2
        first_part = int(final_result)
        second_part = int(round((final_result-first_part)*100))
        new_instance = Money(first_part, second_part)
        return new_instance
    
    def __sub__(self, another):
        result1 = self.__tens + self.__hundreds/100 
        result2 = another.__tens + another.__hundreds/100
        final_result = result1 - result2
        if final_result <0:
            raise ValueError(f"a negative result is not allowed")
        else:
            first_part = int(final_result)
            second_part = int(round((final_result-first_part)*100))
            new_instance = Money(first_part, second_part)
            return new_instance

if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1