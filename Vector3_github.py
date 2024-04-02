class Vector3:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def __str__(self):
        return (f"{self.x},{self.y},{self.z}")

    def __add__(self,other):
        if type(other)==int or type(other)==float:
            return Vector3(self.x+other, self.y+other,self.z+other)
        else:
            return Vector3(self.x+other.x,self.y+other.y,self.z+other.z)

    def __sub__(self,other):
        if type(other)==int or type(other)==float:
            return Vector3(self.x-other, self.y-other,self.z-other)
        else:
            return Vector3(self.x-other.x,self.y-other.y,self.z-other.z)
        
    def __mul__(self,other):
        if type(other)==int or type(other)==float:
            return Vector3(self.x*other, self.y*other,self.z*other)
        else:
            return Vector3(self.x*other.x,self.y*other.y,self.z*other.z)
        
    def __radd__(self, other):
        return Vector3(self.x+other,self.y+other,self.z+other)

    def __rsub__(self, other):
        return Vector3(other-self.x,other-self.y,other-self.z)

    def __rmul__(self, other):
        return Vector3(self.x*other,self.y*other,self.z*other)

    def len(self):
        return (self.x**2+self.y**2+self.z**2)**0.5

    def cross(self, other):
        return Vector3(self.y*other.z-self.z*other.y,self.z*other.x-self.x*other.z,self.x*other.y-self.y*other.x)
    
    def dot(self, other):
        return (self.x*other.x+self.y*other.y+self.z*other.z)

    def normalize(self):
        return Vector3(self.x/self.len(),self.y/self.len(),self.z/self.len())

a = Vector3(3,4,2) 
b = Vector3(2,1,0) 

print(a)
print(3+a)
print(a+3)
print(a+b)
print(a-b)
print(3-a)
print(a-3)
print(a-b)
print(a*b)
print(a*3)
print(a.cross(b))
print(a.dot(b))
print(a.normalize())

