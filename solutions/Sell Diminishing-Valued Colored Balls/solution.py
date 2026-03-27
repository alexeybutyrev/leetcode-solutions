# Problem: Sell Diminishing-Valued Colored Balls
# Language: python3
# Runtime: 1297 ms
# Memory: 37.5 MB

class Solution:
    def maxProfit(self, A: List[int], orders: int) -> int:
        A.sort()
        c = Counter(A)
        A = [ [k,v] for k,v in c.items()]
        A = [[0,0]] + A
        ans = 0
        MOD = 10 ** 9 + 7
        while orders and A[-1][0]:
            #print(ans,A)
            b, n = A.pop()
            a = A[-1][0]
            #print(a,b)
            S = b * (b + 1) // 2 - a * (a + 1) // 2
            if orders >= n * (b-a):
                
                orders -= n * (b-a)
                ans += S * n
                A[-1][1] += n
                ans %= MOD
            else:
                
                d, m = divmod(orders,n)
                #print(orders, A, d, m)
                a = b - d
                S = b * (b + 1) // 2 - a * (a + 1) // 2
                ans += S * n 
                ans += m * a
                return ans % MOD
        
        return ans % MOD