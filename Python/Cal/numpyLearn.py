import numpy as np
import mlab
a = np.array([[1,2,3,4],[4,5,6,7]])
print(a)
print(a.dtype)
print(a.shape)

a = np.arange(0,1,0.1)
print(a)

s = "abcdefgh"
print(np.fromstring(s, np.int8))

def func(i):
    return i*2-1

print(np.fromfunction(func, (10,)))
print(np.arange(0, 60, 10).reshape(-1,1))