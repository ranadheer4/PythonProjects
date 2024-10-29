import numpy as np

a=np.zeros(3,dtype='int')
print(a)

#intialize 2/3 matrix
a=np.zeros([2,3])
print(a)

b=np.zeros([2,3,3])
print(b)

#full()
c=np.full([2,5],[9])
print(c)

d=np.full([2,3,4],[12])
print(d)

#random.rand()
a=np.random.rand(2,6)
print(a)

b=np.random.rand(3,2,1)
print(b)

#ones()
o=np.ones([2,4,3])
print(o)

#eyes()
e=np.eye(4)
print(e)

