class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''.join(x.lower() for x in list(s) if x.isalnum())
        pal = ''
        for i in range(len(ss)-1,-1,-1):
            pal = pal + ss[i]

        return pal == ss