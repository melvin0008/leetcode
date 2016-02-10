/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    private int isBalancedHelper(TreeNode root){
        if(root==null){
            return 0;
        }
        int l=isBalancedHelper(root.left);
        if(l==-1){
            return -1;
        }
        int r=isBalancedHelper(root.right);
        if(r==-1){
            return -1;
        }
        if(Math.abs(l-r)>1){
            return -1;
        }
        return Math.max(l,r)+1;
    }
    
    public boolean isBalanced(TreeNode root) {
        if(isBalancedHelper(root)==-1){
            return false;
        }
        return true;
        
    }
}