import numpy as np


ar=np.arange(10,90,10,dtype=float)
print(ar)

#reshape into matrix
b=ar.reshape(2,4)
print(b)

#linspace()
l=np.linspace(10,200,20)
print(l)

ls=np.linspace(10,200,25,endpoint=False,retstep=True)
print(ls)

