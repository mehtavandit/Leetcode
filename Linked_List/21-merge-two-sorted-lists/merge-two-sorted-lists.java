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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if(list1 == null){
            return list2;
        }
        if(list2 == null){
            return list1;
        }

        ListNode head = null;
        ListNode dummy = null;
        int counter = 0;
        
        while(list1!=null && list2!=null)
        {
            if(list1.val <= list2.val)
            {
                ListNode extra_node = new ListNode();
                extra_node.val = list1.val;
                if(counter == 0)
                {
                    head = extra_node;
                    counter = counter + 1;
                    dummy = extra_node;
                    list1 = list1.next;
                }
                else{
                    dummy.next = extra_node;
                    list1 = list1.next;
                    dummy = extra_node;
                }
                
            }
            else{
                ListNode extra_node = new ListNode();
                extra_node.val = list2.val;
                if(counter == 0)
                {
                    head = extra_node;
                    counter = counter + 1;
                    dummy = extra_node;
                    list2 = list2.next;
                }
                else{
                    dummy.next = extra_node;
                    list2 = list2.next;
                    dummy = extra_node;
                }
                
            }
        }

        if(list1!=null){
            dummy.next = list1;
        }
        if(list2!=null){
            dummy.next = list2;
        }
        return head;
    }
}