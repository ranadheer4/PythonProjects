import numpy as np

print(np.__version__)
a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

print(a)

#get specifc element
print(a[1,5])
print(a[1,-2])
print(a[0,:]) #specific row
print(a[:,2]) #specific col
b=a[0,1:6:2]#specific values in row
print(b)
c=a[0,1:-2:2]
print(c)

a[1,6]=20 #update value of 2nd row and 7th col
print(a)

a[:,3]=5#update 3rd cols
print(a)




