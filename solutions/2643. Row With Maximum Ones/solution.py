# Problem: Row With Maximum Ones
# Language: python3
# Runtime: 925 ms
# Memory: 14.4 MB

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ind = 0
        mo = 0
        for i,r in enumerate(mat):
            s = sum(r)
            if s > mo:
                mo = s
                ind = i
                
        return [ind,mo]