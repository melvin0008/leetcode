/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head == null){
            return null;
        }
    
        ListNode slow = head;
        ListNode fast = head;
        ListNode prev= null;
        
          
        int i=1;
        while(i!=n){
            fast=fast.next;
            i++;
        }
        while(fast.next!=null){
            fast=fast.next;
            prev=slow;
            slow=slow.next;
        }
        
        if(prev==null){
             return head.next;
        }
        prev.next=slow.next;
        slow.next=null;
        return head;
    }
}