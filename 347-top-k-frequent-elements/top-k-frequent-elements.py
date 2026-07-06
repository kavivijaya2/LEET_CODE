class Solution:
    def topKFrequent(self, nums, k):
        count = {}

        # Count frequency of each number
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Create buckets
        freq = [[] for i in range(len(nums) + 1)]

        # Place numbers into their frequency bucket
        for num, c in count.items():
            freq[c].append(num)

        # Collect k most frequent elements
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res        