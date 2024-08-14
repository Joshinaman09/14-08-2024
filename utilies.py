class Square:

    def area(self,side): #definiting method with 1 argument

        return side*side

class Rectangle(Square):

    def Area(self,length,breadth): #overriding method with 2 arguments

        return length*breadth

class Circle(Square):

    def Area(self,radius):

        return 2*3.14*radius*radius #overriding method with 1 argument

sqr = Square()

rct = Rectangle()

crc = Circle()

print(sqr.Area(12))

print(rct.Area(12,10))

print(crc.Area(6))