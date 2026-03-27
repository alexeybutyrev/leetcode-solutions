# Problem: Most Profit Assigning Work
# Language: python3
# Runtime: 407 ms
# Memory: 17.1 MB

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        A = [(d,p) for p,d in zip(profit,difficulty)]
        A.sort()
        D = [d for d,p in A]
        P = [p for d,p in A]
        
        N = len(A)
        for i in range(1,N):
            P[i] = max(P[i-1], P[i])
        #print(P)
        #print(D)
        ans = 0
        for w in worker:
            ind = bisect_right(D,w)
            if ind == 0 and D[ind] > w:
                continue
            if ind == N or D[ind]>=w: ind -=1
            #print(ind,w, D[ind], P[ind])
            ans += P[ind]
        return ans