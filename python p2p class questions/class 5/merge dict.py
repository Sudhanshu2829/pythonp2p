n1=int(input("enter no. of keys for first dict."))
n2=int(input("enter no. of keys for second dict."))
d1=dict([map(eval,input("enter key value pairs for first dict.").split()) for x in range(n1)])
d2=dict([map(eval,input("enter key value pairs for second dict.").split()) for x in range(n2)])
d={**d1,**d2}
print("merged dict. is:",d)