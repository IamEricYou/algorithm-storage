import math
import numpy as np


if myvar:=8 == 8:
    print(f"This is always True")


print(myvar) # This is true

def divmod(a, b, /):
    "Emulate the built in divmod() function"
    return (a // b, a % b)

print(divmod(5,4))


def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
    
# e and f are keywords arguments
print(f(1,2,3,4,e=6,f=10))