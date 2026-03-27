# Problem: Remove Adjacent Almost-Equal Characters
# Language: python3
# Runtime: 3223 ms
# Memory: 17 MB

class Solution:
    def removeAlmostEqualCharacters(self, W: str) -> int:
        oa = ord('a')
        A = [ord(x) - oa for x in W]
        N = len(A)
        q = [(0,0,100)]
        
        heappush(q, (0,0,100))
        d = defaultdict(lambda: inf)
        ans = inf
        while q:
            count,i, l = heappop(q)
            if i == N:
                ans = min(ans, count)
                continue
            for x in range(26):
                curr = int(x != A[i])
                if abs(x - l) > 1 and d[(i,x)] > count + curr:
                    d[(i,x)] = count + curr
                    heappush(q, (count + curr, i + 1, x))
        
        return ans
#         seen = {(0,100)}
#         ans = inf
#         for i, count, last in q:
#             if i == N:
#                 ans = min(ans, count)
#             else:
#                 for x in range(26):
#                     if x != last and abs(x - last) > 1 and (i+1,x) not in seen:
#                         seen.add((i+1,x))
#                         q.append((i+1, count + (x != A[i]), x))
        
#         return ans
                