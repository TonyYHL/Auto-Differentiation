from DNsystem import DN, DNexp

def newton_raphson(f,x:float) -> float:
    MAX_ITER = 40
    DEVIATION = 0.00001
    i = 0

    fx = f(DN(x,1))
    y = fx.real
    if y == 0:
        return x

    dydx = fx.epsilon
    next_x = x-y/dydx

    while i<MAX_ITER:
        if abs(0-next_x)<DEVIATION:
            return next_x
        fx = f(DN(next_x,1))
        y = fx.real
        dydx = fx.epsilon

        next_x = next_x-y/dydx

        i+=1
    return None

def f(x):
    return x**2

print(newton_raphson(f,0))