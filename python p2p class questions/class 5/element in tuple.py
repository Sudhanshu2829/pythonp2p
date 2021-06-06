tup1=eval(input("enter elements of tuple:"))
n=eval(input("enter element you want to find:"))
if n in tup1:
    print("the element is present at index ",tup1.index(n))
else:
    print('element is not present in the tuple')