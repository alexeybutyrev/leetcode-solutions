# Problem: Count Number of Teams
# Language: python3
# Runtime: 1568 ms
# Memory: 16.8 MB

from sortedcontainers import SortedList
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def count(rating):
            A = SortedList()
            ans = 0
            c = Counter()
            for x in rating:
                ind = A.bisect(x)
                count = 0
                
                for j in range(ind-1,-1,-1):
                    ans += c[A[j]]
                c[x] = ind
                A.add(x)
            return ans
        
        return count(rating) + count(rating[::-1])