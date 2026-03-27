# Problem: Minimum Number of Operations to Sort a Binary Tree by Level
# Language: python3
# Runtime: 2765 ms
# Memory: 54.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from sortedcontainers import SortedList
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans = 0
        # Python3 program to find
        # minimum number of swaps
        # required to sort an array

        # Function returns the minimum
        # number of swaps required to
        # sort the array
        def minSwaps(arr):
            n = len(arr)

            # Create two arrays and use
            # as pairs where first array
            # is element and second array
            # is position of first element
            arrpos = [*enumerate(arr)]

            # Sort the array by array element
            # values to get right position of
            # every element as the elements
            # of second array.
            arrpos.sort(key = lambda it : it[1])

            # To keep track of visited elements.
            # Initialize all elements as not
            # visited or false.
            vis = {k : False for k in range(n)}

            # Initialize result
            ans = 0
            for i in range(n):

                # already swapped or
                # already present at
                # correct position
                if vis[i] or arrpos[i][0] == i:
                    continue

                # find number of nodes
                # in this cycle and
                # add it to ans
                cycle_size = 0
                j = i

                while not vis[j]:

                    # mark node as visited
                    vis[j] = True

                    # move to next node
                    j = arrpos[j][0]
                    cycle_size += 1

                # update answer by adding
                # current cycle
                if cycle_size > 0:
                    ans += (cycle_size - 1)

            # return answer
            return ans


        # This code is contributed
        # by Dharan Aditya

        def hamming(A,B):
            ans = 0
            for i in range(len(A)):
                if A[i] != B[i]:
                    #ind = bisect_left(B, A[i])
                    ans += 1
                    #A[ind], A[i] = A[i],A[ind]
                    
            return ans // 2
        
        while q:
            A = []
            L = len(q)
            i = 0
            for _ in range(L):
                node = q.popleft()
                x = node.val
                A.append(x)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            
            ans += minSwaps(A)
        return ans