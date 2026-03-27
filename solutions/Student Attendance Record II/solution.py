# Problem: Student Attendance Record II
# Language: python3
# Runtime: 493 ms
# Memory: 20.5 MB

class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1: return 3
        if n == 0: return 0
        
        dp = [1,1,2]
        
        MOD = 10**9 + 7
        i = 2
        while i < n:
            dp.append(sum(dp[-3:]) % MOD)
            i+=1
        
        
        ans = (dp[-2] + dp[-1] + dp[-3]) % MOD
        for i in range(n):
            ans += (dp[i+1] * dp[n-i]) % MOD
            ans %= MOD
        return ans
    