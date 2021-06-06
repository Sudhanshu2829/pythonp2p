list1=list(eval(input("enter elements of list:")))
print("enter the positions that you want to swap")
pos1=int(input("pos1"))
pos2=int(input("pos2"))
print("original list:",list1)
list1[pos1],list1[pos2]=list1[pos2],list1[pos1]
print("list after swapping:",list1)