class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
newRectangle = Rectangle(12, 10)
print("Dimension of Rectangle - Length:, - Length : %d, Width : %d" % (newRectangle.width,newRectangle.length))
print("Area of Rectangle:", newRectangle.area())