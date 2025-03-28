# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # if not head or left == right:
        #     return head

        # nodes = []

        # current = head

        # while current:
        #     nodes.append(current)
        #     current = current.next

        # left_index = left - 1
        # right_index = right - 1

        # while left_index < right_index:
        #     nodes[left_index], nodes[right_index] = nodes[right_index], nodes[left_index]
        #     left_index += 1
        #     right_index -= 1

        # for i in range(len(nodes) - 1):
        #     nodes[i].next = nodes[i+1]
        # nodes[-1].next = None

        # return nodes[0]


        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        for _ in range(left-1):
            pre = pre.next

        curr = pre.next
        prev = None

        for _ in range (right - left + 1):
            nn = curr.next
            curr.next = prev
            prev = curr
            curr = nn

        pre.next.next = curr
        pre.next = prev


        return dummy.next