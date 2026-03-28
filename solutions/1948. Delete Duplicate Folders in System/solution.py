# Problem: Delete Duplicate Folders in System
# Language: python3
# Runtime: 2216 ms
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
        def dfs1(node):
            key = "("
            for c in node.child:
                key += c + dfs1(node.child[c])
            key += ")"
            if key != "()":
                pattern[key].append(node)
            return key
        
        dfs1(root)
        for k in pattern:
            if len(pattern[k]) > 1:
                for c in pattern[k]:
                    c.id = True

        ans = []
        def dfs2(node, path):
            for c in node.child:
                if not node.child[c].id:
                    dfs2(node.child[c], path + [c])
            if path:
                ans.append(path[:])
        dfs2(root,[])
        return ans