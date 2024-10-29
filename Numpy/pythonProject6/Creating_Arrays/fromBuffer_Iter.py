import numpy as np

#frombuffer()
a=b'welcome to NumPy'
b=np.frombuffer(a,dtype='S1',count=2,offset=12)
print(b)

#fromiter()
a=[10,20,30]
b=np.fromiter(a,dtype='S1',count=3)
print(b)


