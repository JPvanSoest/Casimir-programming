import numpy as np

print("Hello World")

def surf(r):
    s = np.pi*r**2
    return(s)

def circumf(r):
    c = 2*np.pi*r
    return(c)

radius = 6
circumference = circumf(radius)
surface = surf(radius)



