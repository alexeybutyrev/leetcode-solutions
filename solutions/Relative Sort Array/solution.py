# Problem: Relative Sort Array
# Language: python3
# Runtime: 32 ms
# Memory: 16.7 MB

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        
        ans = []
        for x in arr2:
            ans.extend(c[x] * [x])
        
        ans2 = []
        s = set(arr2)
        for x in arr1:
            if x not in s:
                ans2.append(x)
        ans2.sort()
        return ans + ans2
                
                