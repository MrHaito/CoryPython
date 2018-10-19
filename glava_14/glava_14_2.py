class Square():
    
    def __init__(self, a):
        self.a = a
        
    def __repr__(self):
        print("{} на {} на {} на {}".format(self.a,self.a,self.a,self.a))
        
square = Square(2)
print(square)