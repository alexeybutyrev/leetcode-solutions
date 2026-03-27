# Problem: Spiral Matrix IV
# Language: python3
# Runtime: 648 ms
# Memory: 54.7 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        A = [[-1] * n for _ in range(m)]
        
        curr = 0
        
        d = [(0,1), (1,0), (0,-1), (-1,0)]
        
        
        x,y = 0,0
        while head:
            A[x][y] = head.val
            nx = x + d[curr][0]
            ny = y + d[curr][1]
            if x < 0 or nx == m or y <0 or ny == n or A[nx][ny] != -1:
                curr += 1
                curr %= 4
                nx = x + d[curr][0]
                ny = y + d[curr][1]
            
            x,y = nx,ny
            
            head = head.next
        
        return A