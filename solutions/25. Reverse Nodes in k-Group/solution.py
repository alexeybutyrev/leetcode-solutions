# Problem: Reverse Nodes in k-Group
# Language: python3
# Runtime: 48 ms
# Memory: 15.3 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if 1 == k:
            return head
        
        def rev(head, k):
            def reverse_ll(head, k):
                first, second = None, head

                while second and k:
                    n = second.next
                    second.next = first
                    first = second
                    second = n
                    k -= 1

                return (first, second)

            h, n = reverse_ll(head,k)
            
            return h
        
        ptr = head
        ktail = None
        
        ans = None
        
        while ptr:
            count = 0
            
            ptr = head
            while count < k and ptr:
                ptr = ptr.next
                count += 1
                
            if count == k:
                
                revHead = rev(head, k)
                
                if not ans:
                    ans = revHead
                
                if ktail:
                    ktail.next = revHead
                    
                ktail = head 
                head = ptr
        
        # attach the final, possibly un-reversed portion
        if ktail:
            ktail.next = head
        
        return ans if ans else head