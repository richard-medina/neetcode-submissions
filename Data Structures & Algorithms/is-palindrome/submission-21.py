class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''.join(x.lower() for x in list(s) if x.isalnum())
        #l = len(ss)
        #if l%2 == 0:
        #    return all(ss[i] == ss[l-i-1] for i in range((l+1)//2))
        #else:
        #    return all(ss[i] == ss[l-i-1] for i in range((l-1)//2))
        return ss == ss[::-1]