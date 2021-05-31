a,b,c=[eval(x) for x in input("enter length of sides of triangle separated by space").split()]
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("the area if triangle with sides",a,b,c,"is",area)
