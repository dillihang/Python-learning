def read_input(question:str, low:int, high:int):

    while True:
        try:

            number = int(input(question))
            
            if low<= number <=high:
                return number
            
        except ValueError:
            pass
        

        print("You must type in an integer between 5 and 10")




def main():

 
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)



main()