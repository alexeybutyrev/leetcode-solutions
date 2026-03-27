# Problem: Count All Valid Pickup and Delivery Options
# Language: python3
# Runtime: 43 ms
# Memory: 13.9 MB

class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        ans = 1
        for i in range(1,2*n+1):
            ans *= i
            
            if i & 1 == 0:
                ans >>= 1
            ans %= MOD
        
        return ans