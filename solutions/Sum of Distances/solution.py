# Problem: Sum of Distances
# Language: python3
# Runtime: 1139 ms
# Memory: 47.7 MB

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        hm = defaultdict(list)
        for i,x in enumerate(nums):
            hm[x].append(i)
        
        ans = [0] * (N := len(nums))
        for x in hm:
            if len(hm[x]) == 1: continue
            
            S = list(accumulate(hm[x]))
            NS = len(S)
            #print(x, hm[x], S)
            for i in range(NS):
                ind = hm[x][i]
                L = ind * (i+1) - S[i]
                R = (S[-1] - S[i]) - ind * (NS - i-1)
                #print(i, ind, L,R)
                ans[ind] = L + R
        return ans
        
                
            