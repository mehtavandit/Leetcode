# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = None

        while slow:
            next_node = slow.next
            slow.next = second_half
            second_half = slow
            slow = next_node

        max_twin_sum = 0

        first_half = head

        while second_half:
            max_twin_sum = max(max_twin_sum, first_half.val + second_half.val)
            first_half  = first_half.next
            second_half = second_half.next

        return max_twin_sum