# Problem: Find Occurrences of an Element in an Array
# Language: python3
# Runtime: 1235 ms
# Memory: 35.1 MB

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        A = []
        
        for i,a in enumerate(nums):
            if x == a:
                A.append(i)
        ans = []
        for i in queries:
            if i - 1 < len(A):
                ans.append(A[i-1])
            else:
                ans.append(-1)
        return ans