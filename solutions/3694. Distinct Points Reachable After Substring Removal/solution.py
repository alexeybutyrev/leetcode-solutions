# Problem: Distinct Points Reachable After Substring Removal
# Language: python3
# Runtime: 511 ms
# Memory: 27 MB

class Solution:
    def distinctPoints(self, S: str, K: int) -> int:
        N = len(S)


        T = S        
        
        curr = [0,0]
        for i,x in enumerate(T):
            if x == 'U': curr[0],curr[1] = curr[0],    curr[1]+1
            if x == 'D': curr[0],curr[1] = curr[0],    curr[1]-1
            if x == 'L': curr[0],curr[1] = curr[0]-1,  curr[1]
            if x == 'R': curr[0],curr[1] = curr[0]+1,  curr[1]
        s = set()
        c = N-1
        for j in range(K):
            x = T[c - j]
            if x == 'U': curr[0],curr[1] = curr[0],    curr[1]-1
            if x == 'D': curr[0],curr[1] = curr[0],    curr[1]+1
            if x == 'L': curr[0],curr[1] = curr[0]+1,  curr[1]
            if x == 'R': curr[0],curr[1] = curr[0]-1,  curr[1]
        s.add((curr[0],curr[1]))
        for i in range(N-1,-1,-1):
            j = i - K
            if j >= 0:
                x = T[j]
                if x == 'U': curr[0],curr[1] = curr[0],    curr[1]-1
                if x == 'D': curr[0],curr[1] = curr[0],    curr[1]+1
                if x == 'L': curr[0],curr[1] = curr[0]+1,  curr[1]
                if x == 'R': curr[0],curr[1] = curr[0]-1,  curr[1]
                x = T[i]
                if x == 'U': curr[0],curr[1] = curr[0],    curr[1]+1
                if x == 'D': curr[0],curr[1] = curr[0],    curr[1]-1
                if x == 'L': curr[0],curr[1] = curr[0]-1,  curr[1]
                if x == 'R': curr[0],curr[1] = curr[0]+1,  curr[1]
                
                s.add((curr[0],curr[1]))
            else:
                break
        return len(s)
            
        