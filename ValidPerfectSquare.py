class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        l, r = 1, n

        while l <= r:
            mid = l + (r - l) // 2

            x = mid * mid
            if x == n:
                return True

            if x > n:
                r = mid - 1
            else:
                l = mid + 1

        return False
