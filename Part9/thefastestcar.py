class Car:

    def __init__(self, make: str, top_speed: int):

        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return str(self.__dict__)
    
    def __repr__(self):
        return str(self.__dict__)
    

def fastest_car(cars: list):
    fastest=0
    for items in cars:
        if items.top_speed > fastest:
            fastest=items.top_speed
            fastestcar=items.make

    
    return fastestcar
    
if __name__=="__main__":

    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)

    cars = [car1, car2, car3, car4]

    print(fastest_car(cars))