class Square():
    
    square_list = []
    
    def __init__(self, a):
        self.a = a
        self.square_list.append(self.a)
        
    def area(self):
        return self.a**2

    def change_size(self, new_size):
        self.a += new_size

square = Square(2)
print(Square.square_list)

square2 = Square(4)
print(Square.square_list)