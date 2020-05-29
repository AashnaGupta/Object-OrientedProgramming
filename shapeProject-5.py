import math

class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return("<" + self.__class__.__name__ + " x=" + str(self.x) + " y=" + str(self.y) + ">")

    def area(self):
        return "Area to be defined by child class."

    def circumference(self):
        return "Perimeter to be defined by my child class."

    def type(self):
        return "Shape"
    


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __repr__(self):
        return ("<" + self.__class__.__name__ + " x=" + str(self.x) + " y=" + str(self.y) + " radius=" + str(self.radius) + ">")
       
    def area(self):
        a = (float(math.pi) * int(self.radius)* int(self.radius))
        print (self.__class__.__name__ + " area: " + str(a))
        
         
    def circumference(self):
        c= (2 * (math.pi) * self.radius)
        print (self.__class__.__name__ + " circumference: " + str(c))

    def type(self):
        return "Circle"      

class Rectangle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def area(self):
        a= self.x * self.y
        print (self.__class__.__name__ + " area: " + str(a))

         
    def perimeter(self):
        p= 2*(self.x + self.y)
        print (self.__class__.__name__ + " perimeter: " + str(p))
        
    def type(self):
        return "Rectangle"
    
class Square(Rectangle):
    def __init__(self, x):
        super().__init__(x, x)
    
    def area(self):
        super().area()
                
    def perimeter(self):
        super().perimeter()

    def type(self):
        return "Square"       

class RightTriangle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def area(self):
        a= ((self.x * self.y)/2)
        print (self.__class__.__name__ + " area: " + str(a))
            
    def perimeter(self):
        p= (self.x + self.y) + float(math.sqrt((self.x**2) + (self.y**2)))
        print (self.__class__.__name__ + " perimeter: " + str(p))

    def type(self):
        return "RightTriangle"
    
def whoAmI(shape):
    print(shape.type())


shape = Shape(10,20)
print(shape)
print()
               
circle = Circle(10,20,5)
print(circle)
circle.area()
circle.circumference()
print()

rectangle = Rectangle(10,20)
print (rectangle)
rectangle.area()
rectangle.perimeter()
print()

righttriangle = RightTriangle(10,20)
print (righttriangle)
righttriangle.area()
righttriangle.perimeter()
print()

square = Square(10)
print (square)
square.area()
square.perimeter()
print()

print ("Checking for polymorphism:")

shape = Circle(1, 2, 3)
whoAmI(shape)

shape = Rectangle(2, 4)
whoAmI(shape)



