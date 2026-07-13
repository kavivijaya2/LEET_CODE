class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}

        for i, ch in enumerate(word):
            if ch.islower():
                last_lower[ch] = i
            else:
                if ch.lower() not in first_upper:
                    first_upper[ch.lower()] = i

        ans = 0

        for ch in last_lower:
            if ch in first_upper and last_lower[ch] < first_upper[ch]:
                ans += 1

        return ans