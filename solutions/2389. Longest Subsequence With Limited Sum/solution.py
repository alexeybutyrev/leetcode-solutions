# Problem: Longest Subsequence With Limited Sum
# Language: python3
# Runtime: 108 ms
# Memory: 14.1 MB

class Solution:
    def answerQueries(self, A: List[int], queries: List[int]) -> List[int]:
        A.sort()
        A = list(accumulate(A))
        ans = []
        for q in queries:
            ans.append(bisect_right(A,q))
        return ans