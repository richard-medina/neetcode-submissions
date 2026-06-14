class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countLetters = [0] * 26

        for i in range (len(s)):
            countLetters[ord(s[i]) - ord('a')] += 1
            countLetters[ord(t[i]) - ord('a')] -= 1
        
        for x in countLetters:
            if x != 0:
                return False
        return True

        