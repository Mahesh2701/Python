from array import *
arr = array('i',[32,35,37,4,10,98])
newArray=array(arr.typecode,( a for a in arr))
for x in newArray:
    print(x)