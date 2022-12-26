import json
from .base import Point
from .triangle import Triangle

class Stations:
    def __init__(self):
        self.points = []
    
    def loadData(self, path : str):
        with open(path, 'r') as inp:
            data = json.load(inp)
            
            for coords in data:
                try:
                    np = Point(coords['location']['lat'], coords['location']['lon'])
                    self.points.append(np)
                except:
                    pass
    
    def minArea(self):
        
        minArea = Triangle([self.points[0], self.points[1], self.points[2]]).getArea()
        
        for i in self.points:
            for j in self.points:
                for k in self.points:
                    if i != j and j != k and i != k:
                        triangle = Triangle([i, j, k])
                        area = triangle.getArea() 
                        
                        if area < minArea:
                            minArea = area
        
        
        return minArea
        
        
        