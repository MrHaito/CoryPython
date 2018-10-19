class Triangle():

    def __init__(self, b, h):
        self.b = b
        self.h = h
        
    def area(self):
        return 0.5*self.b*self.h

triangle1 = Triangle(3,5)
print(triangle1.area()) 