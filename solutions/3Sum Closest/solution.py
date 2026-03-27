# Problem: 3Sum Closest
# Language: python3
# Runtime: 120 ms
# Memory: 14.2 MB

class Solution:
    def threeSumClosest(self, A: List[int], target: int) -> int:
        A.sort()
        N = len(A)
        dist = inf
        ans = inf
        for i in range(N):
            j = i + 1
            k = N - 1
            while j < k:
                s = A[i] + A[j] + A[k]
                
                if s == target:
                    return target
                
                if abs(s - target) < dist:
                    ans = s
                    dist = abs(s - target)
                if s < target:
                    j += 1
                else:
                    k -=1
        
        return ans