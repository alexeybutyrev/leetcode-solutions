# Problem: Arithmetic Subarrays
# Language: python3
# Runtime: 158 ms
# Memory: 16.6 MB

class Solution:
    def checkArithmeticSubarrays(self, A: List[int], L: List[int], R: List[int]) -> List[bool]:
        ans = []
        for l,r in zip(L,R):
            if r-l<2:
                ans.append(True)
                continue
            B =A[l:r+1][:]
            B.sort()
            d = B[1]-B[0]
            for i in range(2,r-l+1):
                if B[i]-B[i-1]!=d:
                    ans.append(False)
                    break
            else:
                ans.append(True)
        return ans
                
                