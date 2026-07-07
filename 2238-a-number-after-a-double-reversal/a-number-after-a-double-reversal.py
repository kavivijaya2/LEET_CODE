class Solution(object):
    def isSameAfterReversals(self, num):
        if num == 0:
            return True

        if num % 10 == 0:
            return False

        return True