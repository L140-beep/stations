from .base import Point

class TriangleError(Exception):
    ...

class Triangle():
    def __init__(self, points : list[Point]):
        if(len(points) != 3 ):
            raise TriangleError("Not 3 points")

        for point in points:
            if(isinstance(point, Point)):
                continue
            else:
                raise TriangleError("Not points")
    
        self.points = points
    
    def getArea(self) -> float:
        p = self.getPerimeter() / 2
        a, b, c = self.getSides()
        
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5
    
    def getPerimeter(self) -> float:
        a, b, c = self.getSides()
        return a + b + c
    
    def getSides(self) -> tuple:
        a = self.points[0].distance_to(self.points[1])
        b = self.points[1].distance_to(self.points[2])
        c = self.points[2].distance_to(self.points[0])
        return a, b, c