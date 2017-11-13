class Point:
    count=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
        Point.count+=1
    def __add__(self, point):
        pointdop=Point(self.x+point.x,self.y+point.y)
        return pointdop
    @staticmethod
    def countkol():
        return Point.count
t1=Point(5,8)
t2=Point(5,2)
t3=t1+t2
print(t3.x)
print(t3.y)
print(Point.countkol())
