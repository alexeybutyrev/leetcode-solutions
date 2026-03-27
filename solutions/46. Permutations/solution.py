# Problem: Permutations
# Language: python3
# Runtime: 40 ms
# Memory: 16.4 MB

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.ans = []
        def backtrack(left,A):
            if not left:
                self.ans.append(A)
            else:
                for x in left:
                    backtrack(left - {x}, A + [x])
        
        backtrack(set(nums), [])
        return self.ans
                