/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummyNode = new ListNode();
        dummyNode.next = head;
        ListNode tempNode = head;
        int size = 0;
        while(tempNode.next!=null){
            size++;
            tempNode = tempNode.next;
        }
        size++;
        tempNode = dummyNode;
        int counter = size - n;
        for(int i=0; i<counter; i++)
        {
            tempNode = tempNode.next;
        }
        if(tempNode.next == null){
            head=null;
            return head;
        }
        tempNode.next = tempNode.next.next;
        return dummyNode.next;
    }
}