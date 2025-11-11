class SimpleDate:
    """
    A simple date class that supports basic date operations.

    Each month is assumed to have 30 days, and each year 360 days.
    The class allows comparison of dates, addition of days, and 
    calculation of day differences between two dates.

    Attributes:
        dd (int): Day of the month.
        mm (int): Month of the year.
        year (int): Year value.

    Methods:
        __lt__(another): Returns True if this date is earlier than another.
        __gt__(another): Returns True if this date is later than another.
        __eq__(another): Returns True if two dates are equal.
        __ne__(another): Returns True if two dates are not equal.
        __add__(days): Returns a new SimpleDate advanced by a given number of days.
        __sub__(another): Returns the number of days between two dates.
        __str__(): Returns a string representation in 'day.month.year' format.
    """
    def __init__(self, dd: int, mm: int, year: int):
        self.dd = dd
        self.mm = mm
        self.year = year

    def __lt__(self, another):
        if self.year<another.year:
            return True
        elif self.year == another.year and self.mm<another.mm:
            return True
        elif self.year == another.year and self.mm == another.mm and self.dd<another.dd:
            return True
        else:
            return False
        
    def __gt__(self, another):
        if self.year>another.year:
            return True
        elif self.year == another.year and self.mm>another.mm:
            return True
        elif self.year == another.year and self.mm == another.mm and self.dd>another.dd:
            return True
        else:
            return False
        
    def __eq__(self, another):
        if self.year == another.year and self.mm == another.mm and self.dd==another.dd:
            return True
        else:
            return False
    
    def __ne__(self, another):
        if self.year != another.year or self.mm != another.mm or self.dd!=another.dd:
            return True
        else:
            return False
        
    def __add__(self, days: int):

        new_dd = self.dd
        new_mm = self.mm
        new_year= self.year

        if self.dd+days < 30:
            new_dd = self.dd + days
            new_object = SimpleDate(new_dd, self.mm, self.year)
        else:
            for i in range(days):
                new_dd +=1
                if new_dd == 30:
                    new_dd=0
                    if new_mm == 12:
                        new_year +=1
                        new_mm = 0
                        new_mm +=1
                    else:
                        new_mm+=1
            
            new_object = SimpleDate(new_dd, new_mm, new_year)
        return new_object
    
    def __sub__(self, another):
        
        self_totaldays = self.year*360 + self.mm *30 +self.dd
        another_totaldays = another.year*360 + another.mm *30 + another.dd

        return abs(self_totaldays - another_totaldays)

    def __str__(self):
        return f"{self.dd}.{self.mm}.{self.year}"


if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)