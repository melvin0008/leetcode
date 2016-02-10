/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
public class Solution {
	public ListNode detectCycle(ListNode a) {
	    ListNode slow=a;
	    ListNode fast=a;
	    while(true){
	        
	        if(fast==null){
	            return null;
	        }
	        fast=fast.next;
	        if(fast==null){
	            return null;
	        }
	        slow=slow.next;
	        fast=fast.next;
	        if(slow==fast){
	            break;
	        }
	    }
	    slow=a;
	    while(fast!=slow){
	        fast=fast.next;
	        slow=slow.next;
	    }
	    return slow;
	    
	}
}
