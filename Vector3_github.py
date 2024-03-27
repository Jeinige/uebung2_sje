class Vector3:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def __str__(self):
        return (f"{self.x},{self.y},{self.z}")

    def __radd__(self,other):
        if type(other)==int or type(other)==float:
            return Vector3(self.x+other, self.y+other,self.z+other)
        else:
            return Vector3(self.x+other.x,self.y+other.y,self.z+other.z)

    def __rsub__(self,other):
        if type(other)==int or type(other)==float:
            return Vector3(self.x-other, self.y-other,self.z-other)
        else:
            return Vector3(self.x-other.x,self.y-other.y,self.z-other.z)
        
    def __rmul__(self,other):
        if type(other)==int or type(other)==float:
            return Vector3(self.x*other, self.y*other,self.z*other)
        else:
            return Vector3(self.x*other.x,self.y*other.y,self.z*other.z)



a = Vector3(3,4,2) 
b = Vector3(2,1,0) 
c = a * b      # Komponentenweise Multiplikation 
print(c) 
d = a.dot(b)   # Skalarprodukt 
e = a.cross(b) # Kreuzprodukt 
