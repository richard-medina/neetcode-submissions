class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        
        strs1 = [i for i in strs]

        for s in strs:
            s_list = []
            for t in strs:
                if len(s) != len(t):
                    continue

                dict_s, dict_t = {}, {}

                for i in range (len(s)):
                    dict_s[s[i]] = 1 + dict_s.get(s[i], 0)
                    dict_t[t[i]] = 1 + dict_t.get(t[i], 0)

                if dict_s == dict_t:
                    s_list.append(t)

            out.append(s_list)
        
        out_s = list(set([tuple(x) for x in out]))

        out_f = [list(x) for x in out_s]

        return out_f


        