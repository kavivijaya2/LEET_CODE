class Solution:
    def minSwaps(self, nums):
        k = sum(nums)      # Total number of 1's

        if k == 0:
            return 0

        nums = nums + nums  # Make the array circular

        count = 0

        # Count 1's in the first window
        for i in range(k):
            if nums[i] == 1:
                count += 1

        maxOnes = count

        # Slide the window
        for i in range(k, len(nums)):
            if nums[i] == 1:
                count += 1
            if nums[i - k] == 1:
                count -= 1

            if count > maxOnes:
                maxOnes = count

        return k - maxOnes