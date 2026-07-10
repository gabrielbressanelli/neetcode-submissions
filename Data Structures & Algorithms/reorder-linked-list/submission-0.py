# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l2 = head.next
        l1=head

        while l2 and l2.next:
            l2 = l2.next.next
            l1 = l1.next

        prev = None
        curr = l1.next
        l1.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        while prev:
            nxt1 = head.next
            nxt2 = prev.next
            head.next = prev
            prev.next = nxt1
            head = nxt1
            prev = nxt2

        return prev


        

        



        

