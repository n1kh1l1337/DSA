nums=list(map(int,input().split(" ")))
k = len(nums)-1
def new_func(nums, k):
    nums[k:], nums[:k] = nums[:k], nums[k:]
new_func(nums, k)
print(nums)
