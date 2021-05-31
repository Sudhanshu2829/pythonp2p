m=int(input("enter first number"))
n=int(input("enter second number"))
x=m
if x%2!=0:
    x+=1
while x>=m and x<=n:
    print(x)
    x+=2