# Problem: Combination Sum
# Language: python
# Runtime: 132 ms
# Memory: 13.5 MB

class Solution(object):
    def combinationSum(self, A, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        A.sort()
        ans = set()
        def dfs(s,l):
            if s == target:
                ans.add(tuple(sorted(l)))
            else:
                for a in A:
                    if s + a <= target:
                        dfs(s + a, l + [a])
                    else:
                        break
        
        dfs(0,[])
        return ans
                
                