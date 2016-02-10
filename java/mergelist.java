/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1==null){
            return l2;
        }
        if(l2==null){
            return l1;
        }
        
        ListNode head1=l1;
        ListNode head2=l2;
        ListNode head3=null;
        if(head1.val<head2.val){
            head3=head1;
            head1=head1.next;
        }
        else{
            head3=head2;
            head2=head2.next;
        }
        ListNode head=head3;
        
        while(head1!=null && head2!=null){
            if(head1.val<head2.val){
                head3.next=head1;
                head3=head3.next;
                head1=head1.next;    
            }
            else{
                head3.next=head2;
                head2=head2.next;
                head3=head3.next;
            }
            
        }
        
        if(head1!=null){
            head3.next=head1;
        }
        else if (head2!=null){
            head3.next=head2;
        }
        return head;
    }
}