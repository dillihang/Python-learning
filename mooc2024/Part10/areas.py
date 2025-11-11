class Rectangle:
   def __init__(self, x: float, y: float):
      self.x = x
      self.y = y

   def area(self):
      return self.x*self.y
   
   def __str__(self):
      return f"{self.__class__.__name__.lower()} {self.x}x{self.y}"
 
class Square(Rectangle):
   def __init__(self, x, y=None):
      if y:
         super().__init__(x, y)
      else:
         super().__init__(x, y=x)
         
         
if __name__ == "__main__":

   square = Square(4)
   print(square)
   print("area:", square.area())