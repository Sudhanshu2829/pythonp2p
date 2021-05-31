a,b,c=(int(x) for x in input("enter three random numbers for comparison separated by space").split())
max=(a if (a>b and a>c) else(b if (b>a and b>c) else c))
print("the maximum number among",a,b,c,"is",max)
