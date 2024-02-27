def binary(arr,x):
    low,high=0,len(arr)-1          # high=5
    mib=0
    while low <= high:
        mid=(low+high)//2          #center value:-(3) nikane ke liye
        if arr[mid]==x:
            return mid
        elif arr[mid] < x:          # 7<39
            low=mid + 1             #low=(2+1=3)
        elif arr[mid]> x:
            high=mid-1
        else:
            return mib
    return -1

arr=[2,3,4,10,40,89]
x=3
retur=(binary(arr,x))
if retur != -1:
    print("found no:-",retur)
else:
    print("the no. is not valid")