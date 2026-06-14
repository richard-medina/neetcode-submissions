class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        Nsorted0 = sorted(nums)
        Nsorted = [Nsorted0[0]]

        for i in range(1, len(nums)):
            if Nsorted0[i] == Nsorted0[i-1]:
                continue
            else:
                Nsorted.append(Nsorted0[i])

        bad_index = [-1]

        for i in range(len(Nsorted)-1):
            if Nsorted[i]< Nsorted[i+1]-1: 
                bad_index.append(i)

        bad_index.append(len(Nsorted)-1)

        largest_good_chain = 0
        extrema_index = [0, 6]

        for i in range(len(bad_index)-1): 
            if bad_index[i+1]-bad_index[i] > largest_good_chain:
                extrema_index = [bad_index[i], bad_index[i+1]]
                largest_good_chain = bad_index[i+1]-bad_index[i] 
        
        return largest_good_chain



