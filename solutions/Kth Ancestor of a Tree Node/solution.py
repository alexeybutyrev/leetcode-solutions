# Problem: Kth Ancestor of a Tree Node
# Language: python3
# Runtime: 794 ms
# Memory: 78.2 MB

class TreeAncestor:
    LOG = 15
    def __init__(self, n: int, parent: List[int]):
        A = dict(enumerate(parent))
        jump = [A]
        for s in range(self.LOG):
            B = {}
            for i in A:
                if A[i] in A:
                    B[i] = A[A[i]]
            jump.append(B)
            A = B
        self.jump = jump
        

    def getKthAncestor(self, node: int, k: int) -> int:
        s = self.LOG
        while k > 0 and node > -1:
            if k >= 1 << s:
                node = self.jump[s].get(node,-1)
                k-= 1 << s
            else:
                s -= 1
        return node
            


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)