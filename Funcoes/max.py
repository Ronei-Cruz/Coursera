def maximo(x, y, z):
    if x > y and x > z:
        return x
    elif y > z and y > x:
        return y
    elif z > y and z > x:
        return z
    elif x == y and x == z:
        return x
