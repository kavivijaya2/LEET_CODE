class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        pCount = {}
        sCount = {}

        # Count characters in p
        for ch in p:
            pCount[ch] = pCount.get(ch, 0) + 1

        left = 0
        result = []

        for right in range(len(s)):
            sCount[s[right]] = sCount.get(s[right], 0) + 1

            # Keep window size equal to len(p)
            if right - left + 1 > len(p):
                sCount[s[left]] -= 1
                if sCount[s[left]] == 0:
                    del sCount[s[left]]
                left += 1

            # Compare frequency maps
            if sCount == pCount:
                result.append(left)

        return result
        