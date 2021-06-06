list1=list(eval(input("enter elements of list")))
uniq_list=[]
for i in list1:
    if i not in uniq_list:
        uniq_list.append(i)
print(uniq_list)
