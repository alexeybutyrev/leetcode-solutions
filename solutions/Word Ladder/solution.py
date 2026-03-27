# Problem: Word Ladder
# Language: python3
# Runtime: 116 ms
# Memory: 18 MB

from collections import defaultdict, deque
class Trie:
    def __init__(self):
        self.children = {}
    def add(self, word):
        if not self.children:
            self.children[""] = Trie()
            
        curr= self.children[""]
        root = curr
        for l in word:
            if l not in curr.children:
                curr.children[l] = Trie()
            curr = curr.children[l]
        curr.children["$"] = Trie()
        return root
        
    def is_in(self, word):
        n = len(word)
        if "" not in self.children:
            return False
        
        curr = self.children[""]
        for l in word:
            if l not in curr:
                return False
            else:
                curr = curr.children[l]
        
        return True
    
    def check_next(self, word, visited):
        n = len(word)
        q = []
        def check(t, i = 0, w = "", diff = False):
            if i == n:
                if diff and w not in visited:
                    q.append(w)
            else:
                if word[i] in t.children:
                    check(t.children[word[i]], i + 1, w + word[i], diff)
                for l in t.children:
                    if l == word[i]:
                        check(t.children[l], i + 1, w + l, diff)
                    else:
                        if not diff:
                            check(t.children[l], i + 1, w + l, True)
            
        check(self.children[""])
        return q
    
    
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        L = len(wordList[0])
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        graph = defaultdict(list)
        for u in wordList:
            for i in range(L):
                graph[u[:i] + "*" + u[i+1:]].append(u)
        

        visited = set()
        visited.add(beginWord)
        q = deque([beginWord])
        
        count = 1
        while q:
            l = len(q)
            for _ in range(l):
                w = q.popleft()
                if w == endWord:
                    return count

                for i in range(L):
                    wi = w[:i] + "*" + w[i+1:]
                    for v in graph[wi]:
                        if v not in visited:
                            q.append(v)
                            visited.add(v)
            
            count += 1
        return 0