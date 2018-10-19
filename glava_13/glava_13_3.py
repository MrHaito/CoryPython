class Shape():
    def what_am_i(self):
        print("Я - фигура")

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def area(self):
        return self.a*self.b
    
class Square(Shape):
    def __init__(self, a):
        self.a = a
        
    def area(self):
        return self.a**2

    def change_size(self, new_size):
        self.a += new_size


        
a_square = Square(10)
print(a_square.what_am_i())