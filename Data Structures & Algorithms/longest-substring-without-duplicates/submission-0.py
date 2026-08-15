class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check_set = set()
        longest = 0
        j = 0
        for i in range(len(s)):
            while s[i] in check_set:
                check_set.remove(s[j])
                j += 1
            
            w = i-j + 1
            longest = max(longest, w)
            check_set.add(s[i])

        return longest