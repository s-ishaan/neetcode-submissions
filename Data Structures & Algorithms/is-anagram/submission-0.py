class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        size1 = len(s)
        size2 = len(t)
        letters = {}
        if size1 != size2:
            return False
        else:
            for i in s:
                if i not in letters:
                    letters[i] = 1
                else:
                    letters[i] += 1
            for j in t:
                if j in letters and letters[j] != 0:
                    letters[j] -= 1
                else:
                    return False
        return True
                

