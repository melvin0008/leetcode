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
    
    private boolean isValidBSTHelper(TreeNode root, long min,long max){
        if(root==null){
            return true;
        }   
        if(root.val<=min || root.val>=max){
            return false;
        }
        return isValidBSTHelper(root.left,min,root.val) && isValidBSTHelper(root.right,root.val,max);
    }
    
    public boolean isValidBST(TreeNode root) {
        if(root==null){
            return true;
        }
        return isValidBSTHelper(root,Long.MIN_VALUE,Long.MAX_VALUE);
    }
}