list1=list(eval(input("enter elements of list:")))
unwanted=[0,4,5]
for i in unwanted:
    del list1[i]
print("after removing unwanted elements new list is:",list1)