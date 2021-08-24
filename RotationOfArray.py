arr=list(map(int,input().split(" ")))
for i in range(len(arr)):
    arr[-1]=arr[0]
    arr[i]=arr[i+1]
print(arr)