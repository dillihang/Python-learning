import math

def hypotenuse(leg1: float, leg2: float):

    """calculating right angle of an orthogonal triangle c = √(a² + b²) """

    a=leg1**2
    b=leg2**2

    result = a+b

    return math.sqrt(result)



if __name__=="__main__":

    print(hypotenuse(3,4))
    print(hypotenuse(5,12))
    print(hypotenuse(1,1))