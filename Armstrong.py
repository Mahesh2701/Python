a = int(input("Enter A Number"))
s1=a
s=0
while(a>0):
    r=a%10
    s=s+r**3
    a=a//10
print(s)
if(s1==s):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")