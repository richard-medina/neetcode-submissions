class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers)-1

        num1 = numbers[index1]
        num2 = numbers[index2]

        while num1 + num2 != target:
            if num1 + num2 < target:
                index1 += 1
                num1 = numbers[index1]
            if num1 + num2 > target:
                index2 -= 1
                num2 = numbers[index2]
        
        return [index1+1, index2+1]