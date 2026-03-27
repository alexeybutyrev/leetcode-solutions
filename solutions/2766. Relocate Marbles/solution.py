# Problem: Relocate Marbles
# Language: python3
# Runtime: 867 ms
# Memory: 37.8 MB

class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        A = set(nums)
        
        for x,y in zip(moveFrom, moveTo):
            A.remove(x)
            A.add(y)
        return sorted(A)