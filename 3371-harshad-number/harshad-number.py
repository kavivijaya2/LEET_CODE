class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x):
        n = x
        digit_sum = 0

        while n > 0:
            digit_sum += n % 10
            n //= 10

        if x % digit_sum == 0:
            return digit_sum
        else:
            return -1