# Problem: Count Mentions Per User
# Language: python3
# Runtime: 48 ms
# Memory: 18.2 MB

class Solution:
    def countMentions(self, N: int, A: List[List[str]]) -> List[int]:

        M = {"OFFLINE": 1, "MESSAGE": 2}
        A.sort(key = lambda x: (int(x[1]),M[x[0]]))

        T = [0] * N
        ANS = [0] * N
        ALL = [x for x in range(N)]
        for m, t, u in A:
            t = int(t)
            if m == 'OFFLINE':
                u = u.replace('id', '')
                U = map(int, u.split(" "))
                for x in U:
                    T[x] = int(t) + 60
            else:
                if u == "ALL":
                    U = ALL
                elif u == "HERE":
                    U = set()
                    for x in ALL:
                        if T[x] <= t:
                            U.add(x)
                else:
                    u = u.replace('id', '')
                    U = map(int, u.split(" "))
            
                for x in U:
                    ANS[x] += 1
                    
        return ANS