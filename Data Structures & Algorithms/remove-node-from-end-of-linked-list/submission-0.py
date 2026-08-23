# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        size = 0
        while curr:
            size+=1
            curr = curr.next

        if size == 0:
            return head

        remove = size - n

        if remove == 0:
            return head.next
        
        curr = head
        j = 0
        prev = None
        while curr:
            if j != remove:
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                break
            j += 1
        return head

