# Problem: Sort the People
# Language: python3
# Runtime: 103 ms
# Memory: 17.1 MB

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        A = [(-h,n) for h,n in zip(heights,names)]
        A.sort()
        return [n for h,n in A]
    