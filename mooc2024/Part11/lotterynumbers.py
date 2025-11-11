class LotteryNumbers:
    def __init__(self, week: int, win_numb: list):
        self.week = week
        self.win_numb = set(win_numb)

    def number_of_hits(self, numbers: list):
        return len([numb1 for numb1 in numbers if numb1 in self.win_numb])
    
    def hits_in_place(self, numbers: list):
        return [numb1 if numb1 in self.win_numb else -1 for numb1 in numbers]
        

if __name__ == "__main__":
    week5 = LotteryNumbers(5, [1,2,3,4,5,6,7])
    my_numbers = [1,4,7,11,13,19,24]

    print(week5.number_of_hits(my_numbers))

    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.hits_in_place(my_numbers))

