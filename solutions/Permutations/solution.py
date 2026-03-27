# Problem: Permutations
# Language: python3
# Runtime: 3 ms
# Memory: 18 MB

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ANS = []

        def backtrack(left,ans):
            if not left:
                ANS.append(ans)
            else:
                for x in left:
                    if x not in ans:
                        backtrack(left - {x}, ans + [x])


        backtrack(set(nums),[])
        return ANS