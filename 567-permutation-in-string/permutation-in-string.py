class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        s1Count = {}
        s2Count = {}

        # Count characters in s1
        for ch in s1:
            s1Count[ch] = s1Count.get(ch, 0) + 1

        left = 0

        for right in range(len(s2)):
            s2Count[s2[right]] = s2Count.get(s2[right], 0) + 1

            # Keep window size equal to len(s1)
            if right - left + 1 > len(s1):
                s2Count[s2[left]] -= 1
                if s2Count[s2[left]] == 0:
                    del s2Count[s2[left]]
                left += 1

            # Check if current window is a permutation
            if s2Count == s1Count:
                return True

        return False
        