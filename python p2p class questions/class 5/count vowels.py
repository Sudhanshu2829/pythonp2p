str1=input("enter a string")
vowels=set("aeiouAEIOU")
c=0
for i in str1:
    if i in vowels:
        c+=1
print("total no.of vowels=",c)
