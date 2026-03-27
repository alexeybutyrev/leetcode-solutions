# Problem: Partition Array According to Given Pivot
# Language: python3
# Runtime: 2329 ms
# Memory: 31.8 MB

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        L = []
        R = []
        M = []
        for a in nums:
            if a < pivot:
                L.append(a)
            elif a > pivot:
                R.append(a)
            else:
                M.append(a)
        
        return L + M + R