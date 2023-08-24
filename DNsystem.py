"""
Implementation of dual number system represented as a + bE.\n
Support arithmetic operations, exponent, and natural logorithme.
ddx function returns the value of the first derivative of a given function at a given value of x.
"""

from math import exp, log , e, sin, cos, tan, sinh, cosh, tanh

class DN():
    def __init__(self,real:float=0,epsilon:float=0) -> None:
        self.real = real
        self.epsilon = epsilon
    
    def __add__(self,b):
        if type(b) == DN:
            return DN(self.real+b.real,self.epsilon + b.epsilon)
        else:
            return DN(self.real+b,self.epsilon)  
    def __radd__(self,b):
        if type(b) == DN:
            return DN(self.real+b.real,self.epsilon + b.epsilon)
        else:
            return DN(self.real+b,self.epsilon)
    
    def __sub__(self,b):
        if type(b) == DN:
            return DN(self.real-b.real,self.epsilon - b.epsilon)
        else:
            return DN(self.real-b,self.epsilon)
    def __rsub__(self,b):
        if type(b) == DN:
            return DN(self.real-b.real,self.epsilon - b.epsilon)
        else:
            return DN(self.real-b,self.epsilon)
    
    def __mul__(self,b):
        if type(b) == DN:
            return DN(self.real*b.real,self.real * b.epsilon + b.real * self.epsilon)
        else:
            return DN(self.real*b,self.epsilon*b)
    def __rmul__(self,b):
        if type(b) == DN:
            return DN(self.real*b.real,self.real * b.epsilon + b.real * self.epsilon)
        else:
            return DN(self.real*b,self.epsilon*b)
    
    def __truediv__(self,b1):
        if type(b1) != DN:
            b = DN(b1,0)
        else:
            b = b1
        return DN(self.real/b.real,self.epsilon/b.real-self.real*b.epsilon/pow(b.real,2))
    def __rtruediv__(self,b1): # UNPROVEN
        if type(b1) != DN:
            b = DN(b1,0)
        else:
            b = b1
        return DN(self.real/b.real,self.epsilon/b.real-self.real*b.epsilon/pow(b.real,2)) 

    def __pow__(self,b):
        if type(b) == DN:
            apc = self.real ** b.real
            c = b.real
            vb = self.epsilon
            d = b.epsilon
            a = self.real
            return DN(apc,c*a**(c-1)*vb+apc*d*log(a))
        else:
            return DN(self.real**b,b*self.real**(b-1)*self.epsilon)
    def __rpow__(self,b): # UNPROVEN
        if type(b) == DN:
            apc = self.real ** b.real
            c = b.real
            vb = self.epsilon
            d = b.epsilon
            a = self.real
            return DN(apc,c*a**(c-1)*vb+apc*d*log(a))
        else:
            return DN(self.real**b,b*self.real**(b-1)*self.epsilon)

    def __repr__(self) -> str:
        return f"{self.real}+{self.epsilon}E"

def DNexp(x:DN) -> DN:
    a = exp(x.real)
    rtn = DN(a,a*x.epsilon) if type(x) == DN else DN(a,0)
    return rtn if rtn.epsilon == 0 else rtn.real

def DNlog(x:DN) -> DN: return DN(log(x.real),x.epsilon/x.real)

def DNsum(x:list) -> DN: return DN(sum([dn.real for dn in x]),sum([dn.epsilon for dn in x]))

def DNsin(x:DN) -> DN: return DN(sin(x.real),x.epsilon*cos(x.real)) if type(x) == DN else sin(x)

def DNcos(x:DN) -> DN: return DN(cos(x.real),x.epsilon*-sin(x.real)) if type(x) == DN else cos(x)

#def DNtan(x:DN) -> DN: return DN(tan(x.real),x.epsilon*sec(x.real)) if type(x) == DN else tan(x)


#def taylorlog(x:DN) -> DN: return DNsum([pow( (x-DN(1,0))/(x+DN(1,0)) ,2*i+1) * DN(1/(2*i+1),0) for i in range(23)])*2 if x.real != 0 else ZeroDivisionError

def ddx(f,x): return f(DN(x,1)).epsilon
