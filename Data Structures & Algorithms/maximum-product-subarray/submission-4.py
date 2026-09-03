class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {0:[nums[0], nums[0]]}
        t1 = t2= t3 = None
        for i in range(1,n):
            t1 = memo[i-1][1]*nums[i]
            t2 = memo[i-1][0]*nums[i]
            t3 = nums[i]

            memo[i] = [min(t1,t2,t3), max(t1,t2,t3)]


        largest = float('-inf')
        for arr in memo.values():
            a,b = arr
            if b > largest:
                largest = b

        return largest
