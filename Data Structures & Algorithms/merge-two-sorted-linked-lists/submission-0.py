# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l, r = list1, list2
        if not l:
            return r
        if not r:
            return l
        if l.val >= r.val:
            head = r
            r = r.next
        else:
            head = l
            l = l.next
        tail = head
        while l and r:
            if l and r and l.val >= r.val:
                tail.next = r
                r = r.next
            elif l and r and r.val > l.val:
                tail.next = l
                l = l.next
            tail = tail.next
        if l == None:
            tail.next = r
        elif r == None:
            tail.next = l
        return head

            
