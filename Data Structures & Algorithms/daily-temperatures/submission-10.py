class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures) 
        results = []
        for i in range(len(temperatures)):
            for j in range(i, len(temperatures)):
                d = 0
                if temperatures[j] > temperatures[i]:
                    d = j - i
                    break
            results.append(d)
        
        return results
                