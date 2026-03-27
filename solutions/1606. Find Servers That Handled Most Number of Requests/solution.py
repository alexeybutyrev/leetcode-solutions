# Problem: Find Servers That Handled Most Number of Requests
# Language: python3
# Runtime: 3357 ms
# Memory: 38.3 MB

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        hA = []
        for x in range(k):
            heappush(hA, x)
        h = []
        c = Counter()
        for j,(a,l) in enumerate(zip(arrival,load)):
            while h and h[0][0] <= a:
                _,i = heappop(h)
                heappush(hA,j + (i-j)%k)
            if hA:
                i = heappop(hA) % k
                heappush(h,(a + l,i))
                c[i] += 1
        x = max(c.values())
        ans = []
        for i in range(k):
            if c[i] == x:
                ans.append(i)
        return ans
                
            
            