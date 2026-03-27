# Problem: Lexicographically Smallest Generated String
# Language: python3
# Runtime: 2784 ms
# Memory: 17.9 MB

from string import ascii_lowercase
class Solution:
    def generateString(self, S: str, P: str) -> str:
        N, M = len(S), len(P)
        LP = list(P)
        SIZE = N + M - 1
        ANS = ['*'] * SIZE

        for i,x in enumerate(S):
            if 'T' == x:
                ANS[i:i+M] = P
        

        # check if str is illegal
        for i,x in enumerate(S):
            if ('T' == x and ANS[i:i+M] != LP) or ('F' == x and ANS[i:i+M] == LP):
                return ''

        H = hash(P)
        q = deque()

        for i in range(SIZE):
            if i < N and S[i] == 'F':
                q.append((i, hash("".join(ANS[i:i+M]))))
            while q and i - q[0][0] >= M:
                q.popleft()

            if ANS[i] == '*':
                for x in ascii_lowercase:
                    ANS[i] = x
                    for j,h in q:
                        curr = hash("".join(ANS[j:j+M]))
                        if curr == H:
                            break
                    else:
                        ANS[i] = x
                        break
        return "".join(ANS)

                        