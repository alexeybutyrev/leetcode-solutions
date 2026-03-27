# Problem: Sort Even and Odd Indices Independently
# Language: python3
# Runtime: 106 ms
# Memory: 13.9 MB

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        O = []
        E = []
        for i,n in enumerate(nums):
            if i & 1:
                O.append(n)
            else:
                E.append(n)
        O.sort(reverse = True)
        E.sort()
        
        ans = []
        i = j = 0
        while i < len(E) and j < len(O):
            ans.append(E[i])
            ans.append(O[j])
            i += 1
            j += 1
        return ans + E[i:] + O[j:]