class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        index_zero = []

        out = [0]*len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                index_zero.append(i)
        
        if len(index_zero) >= 2:
            return out

        if len(index_zero) == 1:
            prod = 1
            k = index_zero[0]
            for j in range (len(nums)):
                if j == k:
                    continue
                prod = prod * nums[j]
            out[k] = prod
            return out
        
        if len(index_zero) == 0:
            prod = 1
            for j in range (len(nums)):
                prod = prod * nums[j]
            for j in range (len(nums)):
                out[j] = prod//nums[j]
            return out

            

        