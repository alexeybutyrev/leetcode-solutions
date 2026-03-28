# Problem: 4Sum
# Language: python3
# Runtime: 3792 ms
# Memory: 474 MB

class Solution:
    def fourSum(self, A: List[int], target: int) -> List[List[int]]:
        N = len(A)
        
        hm = defaultdict(set)
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    hm[A[i] + A[j] + A[k]].add((i,j,k))
        
        ans = set()
        for i,a in enumerate(A):
            if target - a in hm:
                for s in hm[target - a]:
                    if i not in s:
                        v = [A[i]]
                        for j in s:
                            v.append(A[j])
                        ans.add(tuple(sorted(v)))
        return ans
        