import numpy as np

a=[10,20,30]
b=np.asarray(a,dtype=float)
print(b)

#row major order
a=[[10,20],[30,40]]
b=np.asarray(a,dtype=int,order='c')
print(b)
#convert row major order
for i in np.nditer(b):
    print(i)

#col major order
a=[[10,20],[30,40]]
b=np.asarray(a,dtype=int,order='f')
print(b)
#convert row major order
for i in np.nditer(b):
    print(i)



