# Problem: Sort Even and Odd Indices Independently
# Language: python3
# Runtime: 102 ms
# Memory: 13.8 MB

class Solution:
    def sortEvenOdd(self, A: List[int]) -> List[int]:
        O = A[::2]
        E = A[1::2]
        
        O.sort()
        E.sort(reverse = True)
        
        ans = A[:]
        ans[::2] = O
        ans[1::2] = E
        return ans
        