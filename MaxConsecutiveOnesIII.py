from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        pref = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            pref[i + 1] = pref[i] + nums[i]

        l, r = 0, len(nums)

        def pred(x: int) -> bool:
            flag = 0
            for i in range(len(nums) - x + 1):
                y = pref[i + x] - pref[i]
                if x - y <= k:
                    flag = 1

            return True if flag == 1 else False

        # print(pref)

        while l <= r:
            mid = l + (r - l) // 2

            x = pred(mid)

            # print(x, mid, sep = " ")

            if not x:
                r = mid - 1
            else:
                l = mid + 1

        return l - 1
