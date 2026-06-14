class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        nums1 = []

        for (i, num) in enumerate(nums):
            nums1.append([num, i])
        
        nums1.sort()

        i, j = 0, len(nums) - 1

        while i<j:
            current = nums1[i][0] + nums1[j][0]
            if current == target:
                return [min(nums1[i][1], nums1[j][1]), max(nums1[i][1], nums1[j][1])]
            elif current < target:
                i += 1
            else: 
                j -= 1
        return [] 


