# Problem: Split Linked List in Parts
# Language: python3
# Runtime: 40 ms
# Memory: 15 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        h = head
        N = 0
        while h:
            N += 1
            h = h.next
        
        if N <=k:
            ans = []
            h = head
            for i in range(k):
                if h:
                    h0 = ListNode(h.val)
                    ans.append(h0)
                    h = h.next
                else:
                    ans.append(None)
            return ans
        
        m,l = divmod(N,k)
        #print(m,l)
        h = head
        ans = []
        for i in range(k):
            
            h0 = h
            c = h0
            for _ in range(m + (1 if l else 0)-1):
                h = h.next
                h0 = h0.next
            if l:
                l -= 1
            if h:
                h = h.next
            h0.next = None
            ans.append(c)
        
        return ans