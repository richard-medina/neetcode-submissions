class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = []
        for i in range(len(temperatures)):
            for j in range(i, len(temperatures)):
                l = 0
                if temperatures[j] > temperatures[i]:
                    l = j - i
                    break
            results.append(l)
        
        return results
                