class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        j = 0
        longest = 0
        seen_set = set()
        for i in range(n):
            while s[i] in seen_set:
                seen_set.remove(s[j])
                j+=1

            seen_set.add(s[i])
            longest = max(longest, i-j + 1)

        return longest