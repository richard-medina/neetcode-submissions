class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in range (len(strs)):
            sorteds = ''.join(sorted(strs[i]))
            res[sorteds].append(strs[i])
        
        return list(res.values())
        