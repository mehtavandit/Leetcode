# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """


        nodes = []
        curr = head
        while(curr):
            nodes.append(curr)
            curr = curr.next


        left = 0 #left right are just the indexes, you need nodes[index]
        right = len(nodes) - 1 

        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            if left == right:
                break
            nodes[right].next = nodes[left]
            right -= 1

        nodes[left].next = None
