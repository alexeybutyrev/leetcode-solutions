# Problem: Maximum Number of Integers to Choose From a Range I
# Language: python3
# Runtime: 1251 ms
# Memory: 16 MB

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        
        ans = 0
        s = 0
        for i in range(1,n+1):
            if s + i > maxSum:
                return ans
            else:
                if i not in banned:
                    s += i
                    ans += 1
                
        return ans