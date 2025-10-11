class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.total=0
       
    def add_number(self, number:int):
        
        self.numbers+=1
        self.total+=number

        
    def count_numbers(self):
        
        return self.numbers
    
    def get_sum(self):

        if self.numbers == 0:
            return self.numbers
        
        return self.total

    def average(self):

        if self.numbers == 0:
            return self.numbers
        
        return self.total/self.numbers


def main():

    stats = NumberStats()
    even = NumberStats()
    odd = NumberStats()


    print("Please type in integer numbers:")
    while True:
        numbs = int(input(""))

        if numbs == -1:
            print("Sum of numbers:", stats.get_sum())
            print("Mean of numbers:", stats.average())
            print("Sum of even numbers:", even.get_sum())
            print("Sum of odd numbers:", odd.get_sum())
            break
        else:
            stats.add_number(numbs)
            if numbs%2==0:
                even.add_number(numbs)
            else:
                odd.add_number(numbs)


if __name__=="__main__":

   pass

main()