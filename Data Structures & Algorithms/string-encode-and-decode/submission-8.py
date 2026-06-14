class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        sizes, res = [], []

        for x in strs:
            sizes.append(len(x))
        
        for i in range (len(sizes)):
            res.append(str(sizes[i]))
            res.append(',')
        
        out = ''.join(res + ["#"] + strs)
        return out

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        sizes, res, i = [], [], 0

        while s[i] != '#':
            j = i + 1
            while s[j] != ',':
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1
        
        i += 1
        
        for k in range(len(sizes)):
            res.append(s[i:i+sizes[k]])
            i = i + sizes[k] 
        
        return res

        
