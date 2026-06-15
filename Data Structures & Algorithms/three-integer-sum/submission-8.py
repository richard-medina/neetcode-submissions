class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        numS = sorted(nums)

        for i in range(len(nums)):
            num0 = numS[i]

            nums_alter = numS[:i] + numS[i+1:]

            index1 = 0
            index2 = len(nums_alter)-1

            while index1 < index2:
                num1 = nums_alter[index1]
                num2 = nums_alter[index2]

                sum12 = num1 + num2

                if sum12 == -num0:
                    out.append([num0, num1, num2])
                    index1 += 1
                    index2 -= 1

                if sum12 < -num0:
                    index1 += 1
                
                if sum12 > -num0:
                    index2 -= 1
        
        unique = []

        for i in range(len(out)):
            if sorted(out[i]) in unique:
                continue
            else:
                unique.append(sorted(out[i]))
        return unique

        