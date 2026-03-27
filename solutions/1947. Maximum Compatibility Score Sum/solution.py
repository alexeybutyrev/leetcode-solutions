# Problem: Maximum Compatibility Score Sum
# Language: python3
# Runtime: 2020 ms
# Memory: 14.2 MB

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        S = [int("".join(map(str, s)),2) for s in students]
        M = [int("".join(map(str, s)),2) for s in mentors]
        
        def count_ones(n):
            return bin(n)[2:].count('1')
        K = len(students[0])
        
        N = len(students)
        def dfs(i, mask):
            if i == N:
                return 0
            ans = 0
            for j in range(N):
                if mask & (1 << j) == 0:
                    ans = max(ans, K - count_ones(S[i]^M[j]) + dfs(i+1, mask | (1<<j)))
            
            return ans
        
        return dfs(0,0)