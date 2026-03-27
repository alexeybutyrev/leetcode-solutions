# Problem: Set Intersection Size At Least Two
# Language: python3
# Runtime: 7 ms
# Memory: 19.1 MB

class Solution:
    def intersectionSizeTwo(self, A: List[List[int]]) -> int:
        A.sort(key=lambda x:x[1])
        N = len(A)
        ps,pe = A[0][-1]-1, A[0][-1]
        ans = 2

        for a,b in A[1:]:
            if pe < a:
                ans += 2
                ps,pe = b-1,b
            elif ps < a:
                ans += 1
                if pe != b:
                    ps = pe
                    pe = b
                else:
                    ps,pe = b-1,b
                
        
        return ans
                 