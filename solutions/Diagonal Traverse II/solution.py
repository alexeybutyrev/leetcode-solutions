# Problem: Diagonal Traverse II
# Language: python3
# Runtime: 795 ms
# Memory: 41.3 MB

class Solution:
    def findDiagonalOrder(self, A: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i,a in enumerate(A):
            for j,b in enumerate(a):
                d[i+j].append(b)
        ans = []
        for k in sorted(d.keys()):
            ans.extend(d[k][::-1])
        return ans