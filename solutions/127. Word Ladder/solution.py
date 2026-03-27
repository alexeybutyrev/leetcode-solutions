# Problem: Word Ladder
# Language: python3
# Runtime: 643 ms
# Memory: 20.8 MB

class Node:
    def __init__(self):
        self.t = defaultdict(Node)
        
    def add(self,w):
        curr = self.t
        for l in w:
            curr = curr[l].t
        curr['$'] = w

        

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        T = Node()
        for w in wordList:
            T.add(w)
        
        seen = {beginWord}
        N = len(beginWord)
        def search(w, t):
            ans = []
            
            def local_search(i,t):
                if i == N:
                    if '$' in t.t and t.t['$'] not in seen:
                        ans.append(t.t['$'])
                else:
                    l = w[i]
                    if l == "*":
                        for l2 in t.t:
                            local_search(i+1,t.t[l2])
                    else:
                        if l in t.t:
                            local_search(i+1,t.t[l])
            
            local_search(0,t)
            return ans
        
        
        
        q = deque([beginWord])
        
        steps = 1
        while q:
            L = len(q)
            for _ in range(L):
                word = q.popleft()
                if word == endWord:
                    return steps
                for i in range(len(word)):
                    new_w = word[:i] + "*" + word[i+1:]
                    if new_w not in seen:
                        seen.add(new_w)
                        for w in search(new_w, T):
                            if w not in seen:
                                q.append(w)
            steps += 1
        return 0
        
        
        