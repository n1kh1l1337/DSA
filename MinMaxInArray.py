arr=list(map(int,input().split(" ")))
min=0
max=0
if arr[0]>arr[1]:
    max=arr[0]
    min=arr[1]
else:
    min=arr[0]
    max=arr[1]

for i in range(2,len(arr)):
    if arr[i]>max:
        max=arr[i]
    elif arr[i]<min:
        min=arr[i]
print(min,max)
#print(min(arr),max(arr))