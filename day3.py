########################### numpy arrays ##############################
import numpy as np

#creating a 1D array
a=np.array([60,50,40,30,20,10]) #np.array create numpy array
#list is converting into arrray
print(a)

print(type(a))

#accessing elements
print(a[2])
print(a[4])
print(a[3])
print(a[-2])

#array attributes
print("dimentions",a.ndim)
print("shape",a.shape)
print("size",a.size)
print("datatype",a.dtype)

#can take mixed datatypes and it tries to make all elements the same type
arr=np.array([10,"poras",99.9,True])
print(arr)
#####
ab=np.array([20,10,30.6])
print(ab)
print(ab.dtype)
#converts all elements to float

#nparray can take tuples and lists and nested tupkes and nested lists
#list
p=np.array([1,2,3,4]) 
print("list np.array",p)
#tuple
q=np.array((9,8,7,6))
print("tuple nparray",q)
#two dimentional arrays
#nested list
r=np.array([[20,40,60],[10,30,50]])
print("two dimentional arrays",r)
print(r[1,2])
#nested tuples
s=np.array(((22,33,44),(99,88,77)))
print("nested tuples using numpy",s)

###############################################
#numpy built in functions
#np.zeros()
zeroo=np.zeros(6)
print(zeroo) #default the datatype is set to float

#np.ones()
ar=np.ones(5)
print(ar) #same default dtype is float
num4=np.ones(4,dtype=int)
print(num4)
print(num4.dtype)

#np.arange()
num=np.arange(1,11)# same like range(start,stop,step)
print(num)
#using step in range
num1=np.arange(1,21,2)
print(num1)

#np.linspace()
num2=np.linspace(1,60,num=7,endpoint=True) #can print specific no.of values unlike arange
print(num2)

#########PRINTIG ALL EVEN AND ODD NUMBERS
n=np.arange(1,11,2)
print("odd numbers",n)

##slicing
arr=np.array([1,2,3,4,5,6,7])
print(arr[2:5])
print(arr[:5])
print(arr[3:])
print(arr[::2])
print(arr[::-1])

################## array operations ##########3
arr1=np.array([10,20,30,40,50])
arr2=np.array([1,2,3,4,5])
#addition
print("additon:",arr1+arr2)
#subtraction
print("subract:",arr1-arr2)
#multiplication
print("multiply:",arr1*arr2)
#division
print("division:",arr1/arr2)
#power
print("square",arr1**2)

## numpy fuctions
print("sum:",np.sum(arr1))
print("mean:",np.mean(arr1))
print("maximum",np.max(arr1))
print("minimum:",np.min(arr1))
