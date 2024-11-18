import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pandas as pd
matplotlib.use('TkAgg')


x=np.arange(0,10,2)
print(x)

y= np.linspace(0,10,3)
print(y)

z= np.logspace(0,10,6)
print(z)

x=np.array([1,2,3])
y=np.array([4,2,6])
print("x  = "+ str(x))
print("y  = "+ str(y))
print("_____________________________")
print("x + y  : " + str(x+y))
print("x - y  : " + str(x-y))
print("x * y  : " + str(x*y))
print("x / y  : " + str(x/y))
print("x ** y : " + str(x**y))
print("x // y : " + str(x//y))
print("x % y  : " + str(x%y))



a=np.arange(20)
print(a)
print("*"*50)

print(a.reshape(2,5,2))

print(a.shape)
print(a.ndim)
print(a.size)


z=np.ones((3,4))
print(z)

x=np.zeros((3,4))
print(x)

w=np.array([20,30,40,50])
d=np.arange(4)
print(d)
print(w)
c=w*d

print(c>50)
print(np.sin(c))
