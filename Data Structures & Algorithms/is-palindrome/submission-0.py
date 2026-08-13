class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.replace(" ", "").lower()
        new_s = ''.join(c.lower() for c in s if c.isalnum())
        j = len(new_s) - 1
        i = 0

        while (j >= i):
            if new_s[i] != new_s[j]:
                return False
            i += 1
            j -= 1

        return True