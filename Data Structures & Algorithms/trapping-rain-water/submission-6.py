class Solution:
    def trap(self, height: List[int]) -> int:
        T=0
        for i in range(len(height)):
            left = height[:i]
            right = height[i + 1:]
    
            maxL, maxR = 0, 0
            for x in left:
                maxL = max(maxL, x)

            for x in right:
                maxR = max(maxR, x)
            
            T += max(0, min(maxL, maxR) - height[i])

        return T

