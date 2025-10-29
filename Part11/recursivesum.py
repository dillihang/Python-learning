def recursive_sum(number: int):
    if number<=1:
        return number
    # numb=0
    # for i in range(1, number+1):
    #     numb +=i
    
    return number + recursive_sum(number-1)

        
if __name__ == "__main__":

    result = recursive_sum(3)
    print(result)

    print(recursive_sum(5))
    print(recursive_sum(10))