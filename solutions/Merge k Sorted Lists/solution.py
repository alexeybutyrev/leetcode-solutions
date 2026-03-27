# Problem: Merge k Sorted Lists
# Language: python3
# Runtime: 11 ms
# Memory: 20.3 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        h = []
        for i,l in enumerate(lists):
            if l:
                heappush(h,(l.val, i))
        
        ans = ListNode(-1)
        res = ans
        while h:
            val,i = heappop(h)
            ans.next = ListNode(val)
            ans = ans.next
            lists[i] = lists[i].next
            if lists[i]:
                heappush(h,(lists[i].val,i))
        
        return res.next