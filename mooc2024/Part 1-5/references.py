def double_items(numbers: list):

    numbers_doubled=[]

    for numbs in numbers:
        
        numbers_doubled.append(numbs*2)

    return numbers_doubled






if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)