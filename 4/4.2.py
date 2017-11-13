class Point:
    count=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
        Point.count+=1
    @staticmethod
    def countkol():
        return Point.count
    @classmethod
    def c(cls,x,y):
        return cls(x,y)
ob=Point.c(5,7)
print(ob.x)
print(ob.y)
print(Point.countkol())
