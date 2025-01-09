# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = []

        for temp in lists:
            while temp:
                result.append(temp.val)
                temp = temp.next

        result.sort()

        curr = ListNode(0)
        temp = curr

        for node in result:
            nn = ListNode(node)
            temp.next = nn
            temp = nn

        return curr.next