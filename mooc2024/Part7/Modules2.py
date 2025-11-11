import fractions

def fractionate(amount: int):

    my_list=[]

    for i in range(amount):
        a=fractions.Fraction(1, amount)
        my_list.append(a) 

    return(my_list)





if __name__=="__main__":

    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))