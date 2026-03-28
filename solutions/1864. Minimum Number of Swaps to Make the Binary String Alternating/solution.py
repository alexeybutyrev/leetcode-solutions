# Problem: Minimum Number of Swaps to Make the Binary String Alternating
# Language: python3
# Runtime: 44 ms
# Memory: 14.3 MB

class Solution:
    def minSwaps(self, s: str) -> int:
        
        
        
        ans = inf
        for start in range(2):
            zero = str(start)
            one  = str(start^1)
            misses = [0,0]
            for i,l in enumerate(s):
                target = one if i & 1 else zero
                if l != target:
                    misses[i&1] += 1
            if misses[0] == misses[1]:
                ans = min(ans, misses[0])
        
        return ans if ans != inf else -1