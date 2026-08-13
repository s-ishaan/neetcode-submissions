class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        j = size - 1
        i= 0
        while(j>i):
            sum_nums = numbers[i] + numbers[j]
            if sum_nums > target:
                j -= 1
            elif sum_nums < target:
                i += 1
            else:
                return [i+1,j+1]