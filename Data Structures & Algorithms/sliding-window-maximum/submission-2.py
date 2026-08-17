class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        sub = []

        for i in range(k):
            sub.append(nums[i])

        max_val = max(sub)
        ans.append(max_val)

        for i in range(k, n):
            removed = nums[i-k]

            sub.append(nums[i])
            sub.remove(removed)

            if nums[i] > max_val:
                max_val = nums[i]
            elif removed == max_val:
                max_val = max(sub)

            ans.append(max_val)

        return ans
