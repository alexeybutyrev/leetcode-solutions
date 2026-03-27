# Problem: Recover the Original Array
# Language: python3
# Runtime: 1060 ms
# Memory: 14.8 MB

class Solution:
    def recoverArray(self, A: List[int]) -> List[int]:
        mask = 0
        A.sort()
        N = len(A)
        
        for k2 in {x - A[0] for x in A} - {0}:
            if k2 % 2 == 0:
                c = Counter(A)
                ans = []
                for x in A:
                    if c[x] and c[x + k2]:
                        c[x] -= 1
                        c[x + k2] -= 1
                        ans.append(x + k2//2)

                if 2 * len(ans) == N :
                    return ans
        