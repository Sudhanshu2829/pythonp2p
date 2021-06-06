n=int(input("enter no. of keys for dict."))
d1=dict([map(eval,input("enter key value pairs for first dict.").split()) for x in range(n)])
rem_key=input("enter key to be removed:")
if rem_key in d1:
    del(d1[rem_key])
    print(d1)
else:
    print("key not found in dictionary")