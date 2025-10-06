import random

def lottery_numbers(amount: int, lower: int, upper: int):

    """list random lottery numbers, ammount = number of times it generates random numbers between lower and upper"""

    Lotto_list=[]

    while len(Lotto_list)<amount:

        new_numb=random.randint(lower,upper)

        if new_numb not in Lotto_list:

            Lotto_list.append(new_numb)
    
    return sorted(Lotto_list)
        


if __name__=="__main__":

    for number in lottery_numbers(7, 1, 40):
        print(number)