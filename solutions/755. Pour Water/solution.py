# Problem: Pour Water
# Language: python3
# Runtime: 78 ms
# Memory: 14.1 MB

class Solution:
    def pourWater(self, A: List[int], volume: int, k: int) -> List[int]:
        

        N = len(A)
        
        for _ in range(volume):
            ind = -1
            for i in range(k-1,-1,-1):
                if A[i] < A[i+1]:
                    ind = i
                elif A[i] > A[i+1]:
                    break
            
            if ind != -1:
                A[ind] += 1
                continue
            
            for i in range(k+1,N):
                if A[i] < A[i-1]:
                    ind = i
                elif A[i] > A[i-1]:
                    break
            
            if ind != -1:
                A[ind] += 1
                continue
            else:
                A[k] += 1
        
        return A