x=int(input("Enter Number to check prime or Not"))
count=0;
for i in range(2,x//2 + 1):
    if i%2==0:
        count=count+1
if count==1:

    print("Not-Prime")
else:
    print("Prime")
