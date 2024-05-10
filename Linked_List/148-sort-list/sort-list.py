# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        def merge(left, right):
            dummy = ListNode(-1)
            curr = dummy

            while left and right:
                if left.val <= right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next

            if left:
                curr.next = left
            if right:
                curr.next = right
            
            return dummy.next

        def find_middle(node):

            slow = node
            fast = node.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        middle = find_middle(head)
        right_head = middle.next
        middle.next = None

        sorted_left = self.sortList(head)
        sorted_right = self.sortList(right_head)

        return merge(sorted_left, sorted_right)