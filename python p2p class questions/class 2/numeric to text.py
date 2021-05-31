list1=["one","two","three","four","five","six","seven","eight","nine"]
n=int(input("enter  a number"))
i=n-1
if(i<len(list1)):
    print(list1[i])
else:
    print("number doesn't lie between 0 and 10")