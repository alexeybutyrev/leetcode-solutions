# Problem: Stable Subarrays With Equal Boundary and Interior Sum
# Language: python3
# Runtime: 523 ms
# Memory: 55.4 MB

class Solution:
    def countStableSubarrays(self, A: List[int]) -> int:
        F = [0]

        for x in A:
            F.append(F[-1] + x)

        c = defaultdict(Counter)
        seen = defaultdict(list)
        ans =0
        N = len(A)
        seen[A[0]].append(0)
        c[A[0]][F[1]] += 1
        lans = 0
        for i in range(1,N-1):
            x = A[i+1]
            if x in seen:
                lans += c[x][F[i+1]-x]
            seen[A[i]].append(i)
            c[A[i]][F[i+1]] += 1
        return lans