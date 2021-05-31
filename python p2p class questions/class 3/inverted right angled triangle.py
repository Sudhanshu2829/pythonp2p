rows=int(input("enter the number of rows:"))
for i in range(rows,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()
