class Solution:
    def minSwaps(self, nums):
        n = len(nums)
        ones = sum(nums)

        if ones == 0 or ones == n:
            return 0

        nums = nums + nums

        curr = sum(nums[:ones])
        max_ones = curr

        for i in range(ones, ones + n):
            curr += nums[i]
            curr -= nums[i - ones]
            max_ones = max(max_ones, curr)

        return ones - max_ones