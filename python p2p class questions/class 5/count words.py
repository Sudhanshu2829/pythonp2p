str1=input("enter a sentence")
counts={}
words=[]
words=str1.split()
for i in words:
    c=words.count(i)
    counts[i]=c
print(counts)