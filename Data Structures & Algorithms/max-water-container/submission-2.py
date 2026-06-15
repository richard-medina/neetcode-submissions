class Solution:
    def maxArea(self, heights: List[int]) -> int:
        A = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                A0 = (j-i) * min(heights[i], heights[j])
                
                if A0 > A:
                    A = A0
        
        return A

        