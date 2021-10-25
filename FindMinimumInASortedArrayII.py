from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        while l < len(nums) and nums[l] == nums[r]:
            l += 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[len(nums) - 1]:
                l = mid + 1
            else:
                r = mid

        return nums[l] if l < len(nums) else nums[l - 1]
