# Problem: Maximum Candies You Can Get from Boxes
# Language: python3
# Runtime: 788 ms
# Memory: 27.1 MB

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        
        q = deque()
        for b in initialBoxes:
            q.append(b)
        
        K = set()
        ans = 0
        while q:
            L = len(q)
            v = deepcopy(q)
            for _ in range(L):
                b = q.popleft()
                if status[b] or b in K:
                    ans += candies[b]
                    for c in containedBoxes[b]:
                        q.append(c)
                    for k in keys[b]:
                        K.add(k)
                else:
                    q.append(b)
            if v == q:
                return ans
        return ans