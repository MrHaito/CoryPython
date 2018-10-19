class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def area(self):
        return self.a*self.b
    
class Square():
    def __init__(self, a):
        self.a = a
        
    def area(self):
        return self.a**2
    

rectangle = Rectangle(3,7)
square = Square(3)

print(rectangle.area())
print(square.area())