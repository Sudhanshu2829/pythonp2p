tup1=eval(input("enter elements of tuple:"))
rep=[]
rep_ele={}
c=0
for i in tup1:
    c=tup1.count(i)
    if c>1:
        if i not in rep:
            rep.append(i)
            rep_ele[i]=c
        else:
            continue
    else:
        continue
print("repeated elements are :",*rep,"\n","their repeat count is:",rep_ele)