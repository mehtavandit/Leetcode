# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        counter = 0
        while(head.next):
            head = head.next
            counter = counter+1
            if(counter%2 == 0):
                middle = middle.next
        if(counter%2==1):
            middle=middle.next
        return middle