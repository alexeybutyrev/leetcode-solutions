# Problem: Minimum Operations to Make the Array Alternating
# Language: python3
# Runtime: 1648 ms
# Memory: 34.4 MB

class Solution:
    def minimumOperations(self, A: List[int]) -> int:
        odd = A[::2]
        even = A[1::2]
        
        co = Counter(odd)
        ce = Counter(even)
        
        
        co[-1] = 0
        ce[-2] = 0
        
        O = [(v,k) for k,v in co.items()]
        E = [(v,k) for k,v in ce.items()]
        O.sort(reverse=True)
        E.sort(reverse=True)
        
        if O[0][1] != E[0][1]:
            return len(A) - O[0][0] - E[0][0]
        return len(A) - max(O[1][0] + E[0][0], O[0][0] + E[1][0])
        