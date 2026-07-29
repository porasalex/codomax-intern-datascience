"""python basics"""
#variables and datatypes
name="poras"
age=20
weight=50.5
is_student= True
print("name:",name)
print(type(name))
print("age:",age)
print(type(age))
print("weight:",weight)
print(type(weight))
print("student:",is_student)
print(type(is_student))

#input and output 
a=input("enter the branch:")
print("my branch is",a)

#type casting
b=10
c=float(b)
print(type(c))

#arithmetic operators
p=80
q=6
print("addition:",p+q)
print("subract:",p-q)
print("multiply:",p*q)
print("division:",p/q)
print("floor divison:",p//q)
print("power of or exponent:",p**q)
print("modulus:",p%q)

#comparison opertors
print(p==q)#equal
print(p!=q)#not equal
print(p>q)#greater than
print(p<q)#less than
print(p>=q)#greater or equal to
print(p<=q)#lesstha or equal to

#logical operators true or false
e=True
f=False
print(e and f)
print(e or f)
print(not e)

#assighnment opertors
num=24
num+=4
print(num)
num-=5
print(num)
num*=2
print(num)
num/=2
print(num)

#identity operators returns true or false
a=56
b=a
c=56
print(a is b)
print(a is c)
print(a is not c)

#membership operators
me="poras"
print("po" in me)
print("al" not in me)

#conditional statements
#if-else
#even or odd
n=int(input())
if n%2==0:
    print(n,"is even")
else:
    print(n,"is odd")

#leap year or not
year=int(input())
if year%400==0 or year%4==0 and year%100!=0:
    print(year,"is leap year")
else:
    print(year,"is not leap year")

#loops
#for loop and while loop
#for loop
for i in range(1,11):
    print(i,end=" ")
print()
#printing multipication table
z=10
for i in range(1,11):
    print(z*i,end='')
print()
#printing even and odd numbers up to n
n=int(input())
for i in range(2,n+1,2):
    print(i,end='')

print()

for i in range(1,n+1,2):
    print(i,end='')
print()

#while loop
#fibonacci series
n=int(input())
a,b=0,1
while n<=10:
    print(a,end=' ')
    a,b=b,a+b
    n+=1
print()
#break, continue
for i in range(1,11):
    if i==5:
        break
    print(i,end=" ")
print()
for i in range(1,6):
    if i==3:
        continue
    print(i,end=" ")
print()

#functions
def myself():
    print("i am poras")
def add(a,b):
    return a + b
total=add(10,20)
print("sum:",total)
def square(num):
    return num**2
print(square(4))









