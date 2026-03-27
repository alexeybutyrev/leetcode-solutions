# Problem: Find N Unique Integers Sum up to Zero
# Language: python3
# Runtime: 62 ms
# Memory: 13.9 MB

class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(1,n):
            ans.append(i)
        
        return ans + [-sum(ans)]