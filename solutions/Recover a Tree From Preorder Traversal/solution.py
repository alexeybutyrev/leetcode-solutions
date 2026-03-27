# Problem: Recover a Tree From Preorder Traversal
# Language: python3
# Runtime: 27 ms
# Memory: 18.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> Optional[TreeNode]:
        Q = deque()
        for x in S:
            Q.append(x)
        A = deque()
        while Q:
            if Q[0]=="-":
                c = 0
                while Q and Q[0]=="-":
                    Q.popleft()
                    c += 1
                A.append(str(c) + '-')
                
            else:
                s = ''
                while Q and Q[0] != '-':
                    s += Q.popleft()
                A.append(s)

        
        def solve(A):
            if not A:
                return None
            val = A.popleft()
            
            
            t = TreeNode(int(val))
            if A:
                edge = A.popleft()
                L = deque()
                R = deque()
                while A and A[0] != edge:
                    L.append(A.popleft())
                if A and A[0] == edge:
                    A.popleft()
                R = A
                t.left  = solve(L)
                t.right = solve(R)
            return t
        return solve(A)
