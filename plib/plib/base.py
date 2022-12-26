import json
from typing import Union

class PointError(Exception):
    ...

class Point:
    def __init__ (self, x : Union[int, float], y : Union[int, float]) -> None:    
        self.x = x
        self.y = y
        
    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            if hasattr(other, "__iter__"):
                return self == Point(*other)
            
        return self.x == other.x and self.y == other.y
    
    def __neg__(self) -> "Point":
        return Point(-self.x, -self.y)
    
    def distance_to(self, other: object) -> float:
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5
        
    
    def to_json(self) -> str:
        return json.dumps({"x": self.x, "y": self.y})
    
    @classmethod
    def from_json(cls: type, s: str) -> "Point":
        js = json.loads(s)
        return cls(int(js["x"]), int(js["y"]))
    
    def is_center(self) -> bool:
        return self.x == 0.0 and self.y == 0.0 
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"
    
    def is_center(self) -> bool:
        return self == [0,0]