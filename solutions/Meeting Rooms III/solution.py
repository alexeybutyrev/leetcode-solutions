# Problem: Meeting Rooms III
# Language: python3
# Runtime: 1169 ms
# Memory: 62.3 MB

class Solution:
    def mostBooked(self, n: int, A: List[List[int]]) -> int:
        q = []
        for x in range(n):
            heappush(q,x)
        count = [0] * n
        
        A.sort()
        h = []
        for a,b in A:
            while h and h[0][0] <= a:
                c,ind = heappop(h)
                heappush(q,ind)
            
            if q:
                ind = heappop(q)
                heappush(h,(b,ind))
                count[ind] += 1
            else:
                c,ind = heappop(h)
                count[ind] += 1
                heappush(h,(c+(b-a),ind))

        

        ans = 0
        mx = count[0]
        for i,a in enumerate(count):
            if a > mx:
                ans = i
                mx = a
        
        return ans