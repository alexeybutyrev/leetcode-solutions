# Problem: Number of Pairs of Strings With Concatenation Equal to Target
# Language: python3
# Runtime: 102 ms
# Memory: 14.3 MB

class Solution:
    def numOfPairs(self, A: List[str], target: str) -> int:
        
        s = set()
        count = 0
        for i,st in enumerate(A):
            for j in s:
                if A[j] + st == target:
                    count += 1
                if st + A[j] == target:
                    count += 1
                
            s.add(i)
        
        return count
            