# Problem: Restore The Array
# Language: python3
# Runtime: 1996 ms
# Memory: 21.1 MB

class Solution:
    def numberOfArrays(self, S: str, K: int) -> int:
        if int(S[0]) > K: return 0
        MOD = 10**9 + 7
        dp = [1]
        N = len(S)
        A = []
        for i,x in enumerate(S):
            if x != '0':
                A.append(i)
            else:
                A.append(A[-1])

        #print(A)
        i = 0
        while i < N:
            if int(S[i]) > K: return 0
            
            t = ''
            j = i
            c = 0
            while j >= 0 and int(S[j] + t) <= K:
                t = S[j] + t
                j -= 1
                if S[j+1] != '0':
                    c += dp[j+1]
                    c %= MOD
                else:
                    # jump to non-zero
                    nz = j - A[j+1]
                    j = A[j+1]
                    t = '0' * nz + t
            if c == 0 and S[i] == '0':
                dp.append(c)
                while i < N and S[i] == '0':
                    dp.append(c)
                    i+=1
            else:
                dp.append(c)
                i += 1

        return dp[-1]