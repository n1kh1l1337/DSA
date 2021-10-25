from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        k = int(sqrt(c))
        # print(k)

        for i in range(k + 1):
            n = c - i * i
            # print(n)
            l, r = 0, n

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
