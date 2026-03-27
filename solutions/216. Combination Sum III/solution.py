# Problem: Combination Sum III
# Language: python3
# Runtime: 1925 ms
# Memory: 13.9 MB

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ans = set()
        def backtrack(s,ss):
            if len(s) == k and ss == n:
                ans.add(tuple(sorted(s)))
            else:
                for l in range(1,10):
                    if l not in s and ss + l <=n:
                        backtrack(s | {l}, ss + l)
        
        
        
        backtrack(set(), 0)
        
        return ans
            