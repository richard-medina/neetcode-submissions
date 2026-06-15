class Solution:
    def trap(self, height: List[int]) -> int:
        T=0
        for i in range(len(height)):    
            maxL, maxR = 0, 0
            for x in height[:i]:
                maxL = max(maxL, x)

            for x in height[i + 1:]:
                maxR = max(maxR, x)
            
            T += max(0, min(maxL, maxR) - height[i])

        return T

