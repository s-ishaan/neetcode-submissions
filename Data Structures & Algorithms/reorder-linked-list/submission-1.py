# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = head
        f = head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        
        second = s.next
        s.next = None

        curr = second
        prev = None

        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t

        second = prev
        first = head

        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2
        



        