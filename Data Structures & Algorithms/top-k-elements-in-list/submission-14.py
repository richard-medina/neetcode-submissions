class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        feq = defaultdict(int)

        for i in range (len(nums)):
            feq[nums[i]] = 1 + feq.get(nums[i], 0)
        
        sorted_feq = sorted(list(feq.items()), key = lambda x: x[1], reverse = True)

        out = [sorted_feq[i][0] for i in range(min(k, len(sorted_feq)))]

        return out
        