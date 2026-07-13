from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)

        max_freq = max(count.values())

        ans = 0
        for freq in count.values():
            if freq == max_freq:
                ans += freq

        return ans