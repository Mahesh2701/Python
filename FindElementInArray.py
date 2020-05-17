from array import*
arr = array('i',[12,18,97,76,65,42,7])
value=int(input("Element to be Search"))
for i in range(1,len(arr)):
    if(arr[i]==value):
        print("Found having Index :: ",end="")
        print(i)
        break;
else:
        print("Element Not Found ")
        #python allow us For-Else Loop---
