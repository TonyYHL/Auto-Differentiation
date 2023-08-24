from math import pi

def f(x:float)->float: return x**3

def g(x:float)->float: return sum([1/i**x for i in range(1,9999)])

def bisection(f,x1:float,x2:float)->float:
    """
    Find root in a function within x1 and x2 using the basic bisection technique.\n
    Usage:\n
    def f(x): x**2 
    bisection(f,-2,1) returns 0
    """
    MAX_ITER = 20
    DEVIATION = 0.0001
    x_1 = max(x1,x2)
    x_2 = min(x1,x2)
    new_x = (x1+x2)/2
    y1 = f(x_1)
    y2 = f(x_2)
    if not (y1>0 and y2<0) or (y2>0 and y1<0):
        raise ValueError("Outputs of parameter x1 and x2 must have a different sign.")
    i = 0
    while i < MAX_ITER:
        if abs(abs(x_1) - abs(new_x)) < DEVIATION or abs(abs(x_2) - abs(new_x)) < DEVIATION:
            break
        ym = f(new_x)
        if ym == 0:
            print("Found root")
            return new_x
        elif ym > 0:
            x_1 = new_x
        else:
            x_2 = new_x
        new_x = (x_1+x_2)/2
        i += 1
    print("Found root, total ",i," iterations")
    if MAX_ITER == i :
        return None
    return new_x

print(bisection(g,2,4))

