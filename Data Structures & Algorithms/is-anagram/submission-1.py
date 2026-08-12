class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        size1 = len(s)
        size2 = len(t)
        if size1 != size2:
            return False
        else:
            dict1 = {}
            for letter in s:
                if letter not in dict1:
                    dict1[letter] = 1
                else:
                    dict1[letter] += 1
            
            for letter in t:
                if letter in dict1:
                    if dict1[letter] > 0:
                        dict1[letter] -= 1
                    else:
                        return False
                else:
                    return False

            return True
