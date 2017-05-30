#Datatype
class Operations_Object:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Operations_Object(x,y)
    def __sub__(self,other):
        x = self.x - other.x
        y = self.y - other.y
        return Operations_Object(x,y)
    def __mul__(self,other):
        x = self.x * other.x
        y = self.y * other.y
        return Operations_Object(x,y)

obj1 = Operations_Object(2,7)
obj2 = Operations_Object(2,3) 
obj3 = Operations_Object(7,0)

print "Addition of three instances:",(obj1 + obj2 + obj3)
print "Subtraction of three instance:",(obj1 - obj2 - obj3)
print "Multiplication of three instances:",(obj1 * obj2 * obj3)
