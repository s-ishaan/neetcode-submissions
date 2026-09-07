class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        p = len(s3)

        if m+n!=p:
            return False

        dp = {}

        def dfs(i,j):
            if i ==n and j==m:
                return True
            if (i,j) in dp:
                return dp[(i,j)]
            
            if i < n and s1[i] == s3[i+j] and dfs(i+1,j):
                return True
            if j < m and s2[j] == s3[i+j] and dfs(i,j+1):
                return True
            dp[(i,j)] = False
            return False

        return dfs(0,0)
