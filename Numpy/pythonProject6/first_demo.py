import numpy as np

a=np.array([1,2,3],dtype='int64')
print(a)

b=np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

print(a.ndim)
print(b.ndim)
print(b.shape)
print(a.dtype)
print(a.itemsize)
print(a.size*a.itemsize)
print(a.nbytes)