# Problem: Minimum Operations to Make a Special Number
# Language: python3
# Runtime: 55 ms
# Memory: 16.4 MB

class Solution:
    def minimumOperations(self, S: str) -> int:
        F = []
        T = []
        Z = []
        NN = []
        N = len(S)
        ans = N
        for i in range(N-1,-1,-1):
            if S[i] == '0':
                Z.append(i)
            if S[i] == '2':
                T.append(i)
            if S[i] == '5':
                F.append(i)
            if S[i] == '7':
                NN.append(i)
        T = T[::-1]
        F = F[::-1]
        Z = Z[::-1]
        NN = NN[::-1]
        
        for i in range(N-1,-1,-1):
            if S[i] == '5':
                for j in range(len(T)-1,-1,-1):
                    if T[j] < i:
                        ans = min(ans, i - T[j] - 1 + N - 1 - i)
                        break
                
                for j in range(len(NN)-1,-1,-1):
                    if NN[j] < i:
                        ans = min(ans, i - NN[j] - 1 + N - 1 - i)
                        break
                
            if S[i] == '0':
                ans = min(ans, N - 1)
                for j in range(len(Z)-1,-1,-1):
                    if Z[j] < i:
                        ans = min(ans, i - Z[j] - 1+  N - 1 - i)
                        break
                for j in range(len(F)-1,-1,-1):
                    if F[j] < i:
                        ans = min(ans, i - F[j] - 1+ N - 1 - i)
                        break
        
        return ans