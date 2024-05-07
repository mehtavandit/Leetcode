# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        temp = slow.next
        prev = None
        front = None

        while temp!=None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        first_head = head
        second_head = prev

        while second_head is not None:
            if first_head.val != second_head.val:
                return False

            first_head = first_head.next
            second_head = second_head.next

        return True
