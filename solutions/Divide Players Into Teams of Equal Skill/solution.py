# Problem: Divide Players Into Teams of Equal Skill
# Language: python3
# Runtime: 403 ms
# Memory: 29.5 MB

class Solution:
    def dividePlayers(self, A: List[int]) -> int:
        A.sort()
        N = len(A)
        i = 0
        j = N - 1
        c = None
        ans = 0
        while i < j:
            if c:
                if A[i] + A[j] != c:
                    return -1
            else:
                c = A[i] + A[j]
            ans += A[i] * A[j]
            i += 1
            j -= 1
        return ans
            