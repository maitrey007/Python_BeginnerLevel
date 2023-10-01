class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other) : #FUNCTION TO BE USED FOE OPERATOR OVERLAODING IN ADD OPERATION
        return Vector(self.x+other.x,self.y+other.y)
    
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)
    def __str__(self):
        return "X:{},Y: {}".format(self.x,self.y)
    
v1=Vector(2,6)
v2=Vector(23,45)
v3=v1+v2
print(v3)
