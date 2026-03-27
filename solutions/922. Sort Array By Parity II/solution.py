# Problem: Sort Array By Parity II
# Language: python3
# Runtime: 208 ms
# Memory: 16.7 MB

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        o, e = [], []
        for a in nums:
            if a & 1:
                e.append(a)
            else:
                o.append(a)
        ans = []
        for a,b in zip(o,e):
            ans.append(a)
            ans.append(b)
        return ans