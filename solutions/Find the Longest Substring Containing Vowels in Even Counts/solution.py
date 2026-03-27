# Problem: Find the Longest Substring Containing Vowels in Even Counts
# Language: python3
# Runtime: 559 ms
# Memory: 22.2 MB

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        def f(s):
            c = {}
            c[0]=-1
            m = {x:i for i,x in enumerate(['a', 'e', 'i', 'o','u'])}
            ans =0
            curr = 0
            for i,x in enumerate(s):
                if x in m:
                    curr ^= (1<<m[x])
                if curr not in c:
                    c[curr]=i
                else:
                    ans = max(ans,i-c[curr])
                    
            return ans
        return max(f(s),f(s[::-1]))
                