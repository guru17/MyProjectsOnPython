import math

class Cylinder():
    
    pi = 3.14
    
    def __init__(self, height = 1, radius = 1):
        self.Height = height
        self.Radius = radius
        
    def Volume(self):
        return self.pi * pow(self.Radius, 2) * self.Height
    
    def Surface_Area(self):
        return (2 * self.pi * self.Radius * self.Height) + (2 * self.pi * pow(self.Radius, 2))

class Line:

    def __init__(self, coordinate1, coordinate2):
        self.coor1 = coordinate1
        self.coor2 = coordinate2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return math.sqrt(pow((x2 - x1),2) + pow((y2 - y1),2))

    def slope(self): 
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)
    

