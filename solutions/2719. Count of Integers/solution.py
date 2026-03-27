# Problem: Count of Integers
# Language: python3
# Runtime: 465 ms
# Memory: 21.7 MB

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 +7
        @cache
        def dp(i, num, curr, bound):
            if curr < 0: return 0
            if i ==len(num): return 1
            ans = 0
            if bound:
                for d in range(0,int(num[i])):
                    ans += dp(i+1, num, curr-d, False)
                ans += dp(i+1, num, curr-int(num[i]),True)
            else:
                for d in range(0,10):
                    ans += dp(i+1, num, curr-d, False)
            return ans %MOD
        
    
        return (dp(0,num2,max_sum,True) - dp(0,str(int(num1)-1),max_sum,True) - dp(0,str(int(num2)),min_sum-1,True) + dp(0,str(int(num1)-1),min_sum-1,True))%MOD
                    