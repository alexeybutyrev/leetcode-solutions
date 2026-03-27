# Problem: Partition Labels
# Language: python3
# Runtime: 7 ms
# Memory: 17.8 MB

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def find(s):
            L = [0]
            for x in s:
                d = 1 << (ord(x) - ord('a'))
                L.append(L[-1] | d)
            return L
        
        L = find(s)
        R = find(s[::-1])[::-1]
        stops = []
        ans = []
        for i in range(len(L)):
            if not L[i] & R[i]:
                stops.append(i)
        for j in range(1,len(stops)):
            ans.append(stops[j] - stops[j-1])
        return ans