list1=list(eval(input("enter elements of list:")))
sum=0
for i in list1:
    sum+=i
print("sum=",sum)
print("average=",sum/len(list1))