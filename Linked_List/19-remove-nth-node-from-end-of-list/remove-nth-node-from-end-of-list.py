# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head.next is None:
            head = None
            return head

        temp = head
        counter = 1
        while temp.next is not None:
            temp = temp.next
            counter += 1

        if n == counter:
            head = head.next
            return head


        to_traverse = counter - n

        temp = head
        for i in range(0, to_traverse-1):
            temp = temp.next

        temp.next = temp.next.next

        return head
