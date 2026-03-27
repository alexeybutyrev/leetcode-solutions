# Problem: Alien Dictionary
# Language: python3
# Runtime: 24 ms
# Memory: 14.4 MB

import itertools
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        # Step 0: create data structures + the in_degree of each unique letter to 0.
        graph = defaultdict(set)
        in_degree = Counter({c: 0 for w in words for c in w})
        
        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        
        for w1, w2 in zip(words, words[1:]):
            for l1,l2 in zip(w1,w2):
                if l1 != l2:
                    if l2 not in graph[l1]:
                        graph[l1].add(l2)
                        in_degree[l2] += 1
                    break
            else:
                if len(w2) < len(w1): return ""
        ans = ""
        
        q = deque([k for k, v in in_degree.items() if v == 0])
        while q:

            node = q.popleft()
            ans += node
            for n in graph[node]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    q.append(n)
        if len(ans) < len(in_degree):
            return ""
        
        return ans
        

        
        