class Solution:
    def reverseWords(self, s):
        words = []
        word = ""

        # Extract words manually
        for ch in s:
            if ch != ' ':
                word += ch
            else:
                if word != "":
                    words.append(word)
                    word = ""

        if word != "":
            words.append(word)

        # Build reversed string manually
        result = ""
        for i in range(len(words) - 1, -1, -1):
            result += words[i]
            if i != 0:
                result += " "

        return result
        
        