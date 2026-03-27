# Problem: Take K of Each Character From Left and Right
# Language: python3
# Runtime: 983 ms
# Memory: 32 MB

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        def find(s,k):
            if k == 0:
                return 0
            A = [ord(l) - ord('a') for l in s]

            c = [0,0,0]
            c[A[0]] += 1
            C = [c]
            for a in A[1:]:
                c = C[-1][:]
                c[a] += 1
                C.append(c)

            N = len(A)
            def is_ok(A,B,N):
                for i in range(3):
                    x = B[i] - A[i]
                    if N[i] - x < k:
                        return False
                return True


            i = 0
            j = 0
            ans = -1
            while i < N and j < N:
                if i <= j and j < N and is_ok(C[i],C[j],C[-1]):
                    while i <= j and j < N and is_ok(C[i],C[j],C[-1]):
                        ans = max(ans,j-i)
                        j += 1
                else:
                    j += 1
                i += 1
            return N - ans if ans != -1 else ans
        return min(find(s,k),find(s[::-1],k))
            