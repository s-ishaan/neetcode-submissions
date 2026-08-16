class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1 = ''.join(sorted(s1))
        check_set = set(s1)

        for i in range(len(s2)):
            if s2[i] in check_set:
                check_string = s2[i:i+n]
                check_string = ''.join(sorted(check_string))
                if check_string == s1:
                    return True

        return False