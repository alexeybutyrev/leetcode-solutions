# Problem: Divide Array Into Arrays With Max Difference
# Language: python3
# Runtime: 807 ms
# Memory: 32.4 MB

class Solution:
    def divideArray(self, A: List[int], k: int) -> List[List[int]]:
        A.sort()
        
        i = 0
        ans = []
        while i < len(A):
            x = A[i]
            i +=1
            y = A[i]
            i+= 1
            z = A[i]
            if z - x > k:
                return []
            ans.append([x,y,z])
            i+=1
        return ans
        