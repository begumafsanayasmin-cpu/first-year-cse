x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
print("Addition=",x+y)
print("Substraction=",x-y)
print("Multiplication=",x*y)
print("Division=",x/y)



a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
if (a>b):
    print(a,"is larger")
else:
    print(b,"is larger")


c=int(input("Enter 1st number:"))
d=int(input("Enter 2nd number:"))
e=int(input("Enter 3rd number:"))
if c>d and c>e:
    print(c,"is largest")
elif d>c and d>e:
    print(d,"is largest")
else:
    print(e,"is largest")


m=int(input("Enter 1st number:"))
if(m>0):
    print(m,"is positive")
elif(m<0):
    print(m,"is negative")
else:
    print(m,"is zero")


k=int(input("Enter the number:"))
if k%2==0:
    print(k,"is even")
else:
    print(k,"is odd")


l=int(input("Enter a number:"))
if l>=18:
    print(l,"is elligible for voting")
else:
    print(l,"is not elligible for voting")

