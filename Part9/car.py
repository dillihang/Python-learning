class Car:
    """
    Car class models a simple car with a petrol tank and odometer. 
    The tank has a maximum capacity of 60 litres and the car consumes 
    1 litre of petrol per kilometre. The class provides methods to fill 
    the tank, drive a specified distance (limited by petrol available), 
    and print the current state of the car.
    """
    def __init__(self):
        self.__tank_size = 0
        self.__odometer = 0
    
    def fill_up(self):
        
        self.__tank_size = 60
    
    def drive(self, km: int):
        
        if self.__tank_size-km<0:
            self.__odometer+=self.__tank_size
            self.__tank_size-=self.__tank_size
        else:
            self.__odometer+=km
            self.__tank_size = self.__tank_size-km

    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__tank_size} litres"
        
     
if __name__=="__main__":

    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)

        
