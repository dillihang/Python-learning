class Recording:
    """
    Recording class represents a single recording with a non-negative length in minutes.
    It provides a getter and setter for the length, raising ValueError if a negative
    value is provided.
    """
    def __init__(self, length: int):
        if length<0:
            raise ValueError("Please input only positive numbers")
        else:
            self.__length = length
    
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, length: int):
        if length<0:
            raise ValueError("Please input only positive numbers")
        else:
            self.__length=length
        
     
if __name__=="__main__":

    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)

    
        
