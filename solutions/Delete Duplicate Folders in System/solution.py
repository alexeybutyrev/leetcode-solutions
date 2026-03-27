# Problem: Delete Duplicate Folders in System
# Language: python3
# Runtime: 2112 ms
# Memory: 43 MB

class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.id = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Node()
        
        for p in sorted(paths):
            node = root
            for c in p:
                node = node.child[c]
        
        pattern = defaultdict(list)
        
        def dfs(node):
            if not node:
                return ""
            key = "("
            for c in node.child:
                key += c + dfs(node.child[c])
            
            key += ")"
            if key != "()":
                pattern[key].append(node)
                return key
            return ""

        
        dfs(root)
        
        for k,v in pattern.items():
            if len(v) > 1:
                for n in v:
                    n.id = True
        
        ans = []
        def dfs2(node, l):
            for c in node.child:
                if not node.child[c].id:
                    dfs2(node.child[c], l + [c])
            if l:
                ans.append(l)
            
        dfs2(root, [])
        return ans