# Problem: Maximum Candies You Can Get from Boxes
# Language: python3
# Runtime: 872 ms
# Memory: 27.2 MB

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        S = set(initialBoxes)
        K = set( [i for i,s in enumerate(status) if s])
        
        visited = set()
        ans = 0
        ans_before = -1
        while ans_before != ans:
            ans_before = ans
            next_level_S    = set()
            next_level_keys = set()
            for b in S:
                if b not in visited:
                    if b in K:
                        ans += candies[b]
                        visited.add(b)
                        for k in keys[b]:
                            next_level_keys.add(k)
                            
                        for nb in containedBoxes[b]:
                            next_level_S.add(nb)
                    
            
            next_level_keys |= K
            next_level_S    |= S
            K = deepcopy(next_level_keys)
            S = deepcopy(next_level_S)
    
        return ans