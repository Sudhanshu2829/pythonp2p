rows=int(input("enter no. of rows for pattern:"))
for i in range(0,rows):
    num=1
    for j in range(0,i+1):
        print(num,end=" ")
        num=num+1
    print()