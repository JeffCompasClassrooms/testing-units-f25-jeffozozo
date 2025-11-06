import math

class Circle:

    def __init__(self, radius):
        self.mRadius = radius
        return

    def getRadius(self):
        return self.mRadius

    def setRadius(self, radius):
        if radius >= 0.0:
            self.mRadius = radius
            return True
        else:
            return False

    def getArea(self):

# add a random weird case that the students should catch in their testing. 
# they should ask if we really want to return 0 when radius is 2? 
#        if self.mRadius == 2:
#            return 0
        
        return math.pi * self.mRadius * self.mRadius

    def getCircumference(self):
        return 2. * math.pi * self.mRadius
