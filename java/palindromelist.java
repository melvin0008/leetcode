/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode p=null;
        ListNode q=head;
        while(q!=null){
            ListNode temp=q.next;
            q.next=p;
            p=q;
            q=temp;
            
        }
        return p;
    }
    
    public boolean isPalindrome(ListNode head) {
        ListNode mid= null;
        ListNode slow=head;
        ListNode fast=head;
        if(head==null){
            return true;
        }
        if(head.next==null){
            return true;
        }
        fast=fast.next;
        while(fast!=null && fast.next!=null ){
            slow=slow.next;
            fast=fast.next;
            fast=fast.next;
        }
        
        mid=slow.next;
        slow.next=null;
        ListNode head2=this.reverseList(mid);
        while(head!=null && head2!=null)
        {
            if(head2.val!=head.val){
                return false;
            }
            head=head.next;
            head2=head2.next;
        }
        if((head==null || head.next==null) && head2==null){
            return true;
        }
        return false;
        
    }
}