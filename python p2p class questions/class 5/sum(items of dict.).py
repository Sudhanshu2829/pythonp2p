n=int(input("enter no. of keys for dict."))
d1=dict([map(eval,input("enter key value pairs for first dict.").split()) for x in range(n)])
sum=0
for i in d1:
    sum+=d1[i]
print("sum of items in dict. is:",sum)

