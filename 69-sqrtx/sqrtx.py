class Solution(object):
    def mySqrt(self, x):
        r = 0
        while r * r <= x:
            r += 1
        return r - 1
        