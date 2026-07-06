class Solution:
    def lengthOfLastWord(self, s):
        count = 0
        i = len(s) - 1

        # Skip the spaces at the end
        while i >= 0 and s[i] == " ":
            i -= 1

        # Count the letters of the last word
        while i >= 0 and s[i] != " ":
            count += 1
            i -= 1

        return count
        