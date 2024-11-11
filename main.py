import numpy as np
import matplotlib
import pandas


# arr1=np.array([])
# arr2=np.array([1,2,3])
# arr3=np.array(range(4))
#
#
# print(arr3)
# print(arr3[3])
# print("*******")
# print(arr3[0:-2])
# print(arr3[-3:len(arr3)])
# print(arr3[1:len(arr3)])
# print(arr3[-len(arr3):len(arr3)])

# x= np.array([], dtype=int)
# print(x.dtype)
# y=np.array([],dtype=np.int8)
# print(y.dtype)
# z=np.array([])
# print(z.dtype)
# w=np.array(["ali"])
# print(w.dtype)

x=np.array([],dtype=np.int8)
x=np.append(x,0)
print(x)

x=np.append(x,[-1,1,-2])
print(x)

x=np.append(x,range(2,10))
print(x)

x=np.array([[1,2],[3,4]])
print(x)

print("*******************")
y=np.array(range(9))
print(y)
x=y.reshape((3,3))
print(x)

print(x.shape)
print(x.size)
print(x.shape[0])
print("*"*50)
z=np.array(range(27)).reshape((3,3,3))
print(z)
print(z.size)

print("*"*50)
arr3=np.zeros(5)
arr4=np.ones(5)
print(arr3)
print(arr4)
print("*"*50)
print(np.diag([2,3,4]))
print("*"*50)

p=np.random.rand(3,2)
print(p)

p2=np.random.randint(5, size=20)
print(p2)

p3=np.random.randint(15, size=(2,3))
print(p3)