# Problem: Count Subarrays With More Ones Than Zeros
# Language: python3
# Runtime: 866 ms
# Memory: 33.9 MB

class Solution:
    def subarraysWithMoreZerosThanOnes(self, A: List[int]) -> int:
        A = [1 if a else -1 for a in A]
        
        S = list(accumulate(A, initial=0))
        mn = min(S)
        S = [s - mn + 1 for s in S]
        
        c = Counter()
        curr = 0
        pre = 0
        count = 0
        MOD = 10**9 + 7
        ans = 0
        for x in S:
            if x == pre + 1:
                count += c[pre]
                count %= MOD
            else:
                count -= c[pre-1]
                count %= MOD
            ans += count
            c[x] += 1
            ans %= MOD
            pre = x
        
        return ans