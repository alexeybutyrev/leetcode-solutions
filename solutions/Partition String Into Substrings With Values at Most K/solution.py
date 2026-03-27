# Problem: Partition String Into Substrings With Values at Most K
# Language: python3
# Runtime: 149 ms
# Memory: 15.7 MB

class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        if int(max(list(s))) > k:
            return -1
        
        ans = num = 0
        for d in s:
            num = num * 10 + int(d)
            if num <= k:
                continue
            else:
                ans += 1
                num = int(d)
        
        return ans + 1