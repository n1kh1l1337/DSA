def maxsumSubArray(nums):
    maxsum=0
    cursum=0
    for i in range(len(nums)):
        cursum=cursum+nums[i]
        if(cursum>maxsum):
            maxsum=cursum
        elif(cursum<0):
            cursum=0
    return maxsum
print(maxsumSubArray([-1,-2,-3,4]))