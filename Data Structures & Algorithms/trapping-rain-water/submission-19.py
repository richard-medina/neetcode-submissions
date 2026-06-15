class Solution:
    def trap(self, height: List[int]) -> int:
        T=0
        l = len(height)

        if l == 0: 
            return 0
             
        maxL = [0]*l
        maxR = [0]*l

        maxL[0] = height[0]
        maxR[-1] = height[-1]

        for i in range(l):
            maxL[i] = max(maxL[i-1], height[i])

        for i in range(l-2, -1, -1):
            maxR[i] = max(maxR[i+1], height[i])

        for i in range(len(height)): 
            T += max(0, min(maxL[i], maxR[i]) - height[i])

        return T

