a = int (input("Enter a Number To Check Palindrom"))
s1=a
s=0;
while(a>0):
    r=a%10
    s=s*10+r
    a=a//10
if(s1==s):
    print("Number Is Palindrom")
else:
    print("Number Is Not Palindrom")
