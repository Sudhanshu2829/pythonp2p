print("half pyramid:")
row1=int(input("enter no. of rows:"))
for i in range(1,row1+1):
   for j in range(1,i+1):
        print(j,end=" ")
   print()

print("\ninverted half pyramid:")
row2=int(input("enter no.of rows:"))
for i in range(row2,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("\nfull pyramid:")
row3=int(input("enter the number of rows:"))
for row in range(1,row3+1):
    for space in range(1,row3-row+1):
        print(" ",end=" ")
    k=row
    for j in range(1,row+1):
        print(k,end=" ")
        k+=1
    k=k-2
    for j in range(1,row):
        print(k,end=" ")
        k-=1
    print()

print("\nhollow half pyramid:")
row4=int(input("enter no. of rows:"))
for row in range(1,row4+1):
    for col in range(1,row4+1):
        if(col==1 or row==row4 or row==col):
            print(col,end=" ")
        else:
            print(end="  ")
    print()

print("\ninverted half pyramid:")
row5=int(input("enter no. of rows:"))
for row in range(1,row5+1):
    for col in range(1,row5+1):
        if(row==1) :
            print(col,end=" ")
        elif(col==1):
            print(row,end=" ")
        elif(row+col==(row5+1)):
            print(row5,end=" ")
        else:
            print(" ",end=" ")
    print()

print("\nfull hollow pyramid:")
row6=int(input("enter the no. of rows"))
i,k=1,2
for row in range(1,row6+1):
    for col in range(1,2*row6):
        if(row+col==row6+1):
            print("1",end=" ")
        elif(row==row6 and col!=k):
            print(col-i,end=" ")
            k=k+2
            i=i+1
        elif(col-row==row6-1):
            print(row,end=" ")
        else:
            print(" ",end=" ")
    print()
