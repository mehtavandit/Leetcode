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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode dummy = new ListNode(0);
        ListNode temp = dummy;

        while(l1!=null || l2!=null || carry == 1)
        {
            int result = carry;
            if(l1!=null){
                result += l1.val;
                l1 = l1.next;
            }

            if(l2!=null){
                result += l2.val;
                l2 = l2.next;
            }

            ListNode node = new ListNode (result%10);
            carry = result/10;
            temp.next = node;
            temp = node;
        }

        return dummy.next;
    }
}