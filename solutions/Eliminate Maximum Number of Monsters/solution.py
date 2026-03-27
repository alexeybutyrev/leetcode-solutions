# Problem: Eliminate Maximum Number of Monsters
# Language: python3
# Runtime: 762 ms
# Memory: 38.7 MB

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        A = [(d,s) for d,s in zip(dist,speed)]
        A.sort(key = lambda x: x[0]/x[1])
        
        ans = 0
        for i,(d,s) in enumerate(A):
            cd = i * s
            if cd >= d:
                return i
            ans += 1
        return ans