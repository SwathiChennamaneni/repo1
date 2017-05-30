"""
75. implement class method and instance method and static method
in a class with an example. Create a instance and call all the methods."""
import math

class Calculation(object):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
 
    @staticmethod
    def compute_area(radius):
         return math.pi *(radius ** 2)
 
    @classmethod
    def compute_volume(cls, height, radius):
         return height * cls.compute_area(radius)
 
    def get_volume(self):
        return self.compute_volume(self.height, self.radius)

c = Calculation(2,3)

#Static Method
print "**Static Method**"
print Calculation.compute_area(2)
print c.compute_area(2)
#Class Method
print "\n**Class Method**"
print Calculation.compute_volume(3,4)
print c.compute_volume(3,4)
# Instance Method
print "\n**Instance Method**"
print c.get_volume()
