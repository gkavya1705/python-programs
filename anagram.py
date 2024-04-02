str1=input()
str2=input()
s=[]
v=[]
for i in str1:
   s.append(i)
for i in str2:
    v.append(i)
if sorted(s)==sorted(v):
    print("true")
else:
    print("false")