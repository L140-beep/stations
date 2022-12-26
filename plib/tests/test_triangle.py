import pytest
from plib.triangle import Triangle, TriangleError
from plib.base import Point


@pytest.fixture
def points():
    return Point(0, 0), Point(1 , 0), Point(1, 1)

class TestTriangle():
    def test_init(self, points):
        new_points = points
        
        Triangle(new_points)
        
        with pytest.raises(TriangleError):
            Triangle(new_points[0:1])
                
        with pytest.raises(TriangleError):
            Triangle(["qwe", "wqs", "das"])        
        
    
    def test_getArea(self, points):
        triangle = Triangle(points)
        perimeter = triangle.getPerimeter() / 2
        a = points[0].distance_to(points[1])
        b = points[1].distance_to(points[2])
        c = points[2].distance_to(points[0])
        assert triangle.getArea() == pytest.approx((perimeter * (perimeter - a) * (perimeter - b) * (perimeter - c)) ** 0.5, 0.1)
        
    def test_getPerimeter(self, points):
        triangle = Triangle(points)
        a = points[0].distance_to(points[1])
        b = points[1].distance_to(points[2])
        c = points[2].distance_to(points[0])
        assert triangle.getPerimeter() == a + b + c
    
    def test_getSides(self, points) -> tuple:
        triangle = Triangle(points)
        a = points[0].distance_to(points[1])
        b = points[1].distance_to(points[2])
        c = points[2].distance_to(points[0])
        assert triangle.getSides() == pytest.approx([a, b, c], 0.1)
        
    