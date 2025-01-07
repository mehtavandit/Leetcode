# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        tmp = head

        while(tmp!=None):
            
            tmp = tmp.next
            length += 1


        counter = length - n

        dummy = ListNode()
        dummy.next = head

        tmp = dummy

        for i in range(counter):
            tmp = tmp.next

        tmp.next = tmp.next.next

        return dummy.next