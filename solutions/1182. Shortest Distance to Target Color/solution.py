# Problem: Shortest Distance to Target Color
# Language: python3
# Runtime: 1736 ms
# Memory: 38.8 MB

class Solution:
    def shortestDistanceColor(self, A: List[int], queries: List[List[int]]) -> List[int]:
        d = defaultdict(dict)
        N = len(A)
        hm = {}
        ans = []
        for i,c in queries:
            if (i,c) not in hm:
                for k in range(max(i,N-i)):
                    if i + k < N and A[i+k] == c:
                        hm[(i,c)] = k
                        break

                    if i - k >= 0 and A[i-k] == c:
                        hm[(i,c)] = k
                        break
                else:
                    hm[(i,c)] = -1
            ans.append(hm[(i,c)])
        
        return ans
                