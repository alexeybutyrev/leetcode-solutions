# Problem: Dota2 Senate
# Language: python3
# Runtime: 84 ms
# Memory: 17.8 MB

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        def make_RD(sante):
            R = deque()
            D = deque()
            for i,x in enumerate(sante):
                if x == 'R':
                    R.append(i)
                else:
                    D.append(i)
            return R,D
        
        while senate:
            R,D = make_RD(senate)
            dR,dD = set(),set()
            sR,sD = deque(), deque()
            for i,x in enumerate(senate):
                if x == 'R' and i not in dR:
                    while R[0] != i: R.popleft()
                    R.popleft()
                    if D:
                        dD.add(D.popleft())
                    else:
                        if sD:
                            sD.popleft()
                        else:
                            return "Radiant"
                    sR.append(i)
                    dR.add(i)
                
                if x == 'D' and i not in dD:
                    while D[0] != i: D.popleft()
                    D.popleft()
                    if R:
                        dR.add(R.popleft())
                    else:
                        if sR:
                            sR.popleft()
                        else:
                            return "Dire"
                    sD.append(i)
            S = ""
            while sR and sD:
                ri = sR.popleft()
                di = sD.popleft()
                if ri < di:
                    sD.appendleft(di)
                    S += 'R'
                else:
                    sR.appendleft(ri)
                    S+= 'D'
            while sR:
                sR.popleft()
                S += 'R'
            
            while sD:
                sD.popleft()
                S += 'D'
            senate = S
            
                
                