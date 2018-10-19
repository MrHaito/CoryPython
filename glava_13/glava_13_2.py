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

    def change_size(self, new_size):
        self.a += new_size

a_square = Square(100)
print(a_square.a)

a_square.change_size(100)
print(a_square.a)