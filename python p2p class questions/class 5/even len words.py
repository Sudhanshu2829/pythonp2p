str1=input("enter a string")
s=str1.split()
print("words with even length are:")
for i in s:
    if len(i)%2==0:
        print(i)