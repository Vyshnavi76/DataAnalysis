# -*- coding: utf-8 -*-
"""DA_day1_Numpy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fAPqAmrnFKaMc7mdg74MCz3Wi2rIEt-G
"""

#importing
import numpy as np

!pip install np

"""Arrays"""

#creating 1d array
A=np.array([2,3,4,5])
print(type(A))
print(A)

#creating a 2d array #rows and columns
B=np.array([[2,3,4],[7,8,9]])
print(B)

#creating a 3d array #rows,columns,groups
C=np.array([[[2,3,4],[6,7,8]],[[6,9,0],[2,3,1]]])
print(C)

#checking dimensions
print(A.ndim)
print(B.ndim)
print(C.ndim)

#ones
D=np.ones((2,3,2))
print(D)

#ones
E=np.ones((3,2)) #rows,columns,2d
print(E)

#Zeros
F=np.zeros((3,2))
print(F)

G=np.eye(4)
print(G)

#arange
H=np.arange(3,31,3).reshape(5,2) #prints upto the given range
print(H)

#arange
I=np.arange(5,1001,5)
print(I)

V=np.linspace(13,26,10)  #
print(V)

L=np.arange(1,7).reshape(2,3)
print(L)
R=np.arange(9,15).reshape(2,3)
print(R)

print(L+R)

G=np.sum((L+R))
print(G)

G=np.sum((L,R),axis=0)
print(G)

G=np.sum((L,R),axis=1)
print(G)

h=np.ones((4,2))
g=np.ones((4,2))
print(np.sum((h,g),axis=0))

h=np.ones((4,2))
g=np.ones((4,2))
print(np.sum((h,g),axis=1))

A=np.array([[1,1],[0,1]])
B=np.array([[2,0],[3,4]])
print(A*B)

print(A@B)

"""b=np.array[25,289,361,81]#find square roots and iterate through result values output:5 square is 25..."""

b=np.array([25,289,361,81])
for i in b:
  print(np.sqrt(i),"square is",i)

"""array_joins"""

a=np.array([34,35,36,37,38,39])
a.resize(2,3)
print(a)
print("\n")
b=np.array([4,5,6,7,8,9])
b.resize(2,3)
print(b)
print("\n")
print(np.vstack((a,b)))
print("\n")
print(np.hstack((a,b)))

a=np.arange(30).reshape(2,3,5)#no of groups=2   :2 columns in each group
print(a)                      #no of rows=3     :3 groups formed
print("output of dstack")
print(np.dstack(a))