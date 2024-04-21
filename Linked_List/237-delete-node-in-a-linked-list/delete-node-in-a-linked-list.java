/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        ListNode temp = null;
        while(node.next!=null){
            int x = node.val;
            node.val = node.next.val;
            node.next.val = x;
            temp = node;
            node = node.next;
        }
        temp.next = null;
    }
}