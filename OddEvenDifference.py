def findOddEvenDifference(arr,n):
    odd=0
    even=0
    for i in range(n):
        if (arr[i]%2==0):
            even=even+arr[i]
        else:
            odd=odd+arr[i]
    return odd-even
n=int(input())
arr = [int(x) for x in input().split(" ")]
print(findOddEvenDifference(arr,n))