# Problem: Find All Possible Stable Binary Arrays I
# Language: python3
# Runtime: 5991 ms
# Memory: 148.5 MB

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, L: int) -> int:
        MOD = 10**9 + 7

        @cache
        def dp1(O,Z):
            # we are comming here from one
            # all we can add is zeros
            if O == Z == 0: return 1
            
            ans = 0
            if Z:
                for z in range(1,min(Z+1,L+1)):
                    ans += dp0(O, Z - z)
                    ans %= MOD
            
            return ans
        
        @cache
        def dp0(O,Z):
            # we are comming here from zero
            # all we can add is ones
            if O == Z == 0: return 1
            
            ans = 0
            if O:
                for o in range(1,min(O+1,L+1)):
                    ans += dp1(O-o, Z)
                    ans %= MOD
            
            return ans
        
        ans = dp1(one,zero)
        ans += dp0(one,zero)
        return ans % MOD