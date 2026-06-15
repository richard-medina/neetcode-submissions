class Solution:
    def maxArea(self, heights: List[int]) -> int:
        index1 = 0
        index2 = len(heights)-1
        
        A = (index2 - index1) * min(heights[index2], heights[index1])
        
        while index1 < index2:
            h1 = heights[index1]
            h2 = heights[index2]

            A = max(A, (index2 - index1) * min(h1, h2))
            
            if h1 == h2:
                index1 += 1
            if h1 < h2:
                index1 += 1
            if h1 > h2:
                index2 -= 1
        
        return A

        