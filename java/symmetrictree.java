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
    public boolean isSymmetricHelper(TreeNode left, TreeNode right){
       
        if(left==null && right==null){
            return true;
        }
        else if((left==null && right!=null)||(left!=null && right==null)){
            return false;
        }
        else {
            if(left.val!=right.val){
                return false;
            }
        }
        return isSymmetricHelper(left.left,right.right) && isSymmetricHelper(left.right,right.left);
    }
    public boolean isSymmetric(TreeNode root) {
        if(root==null){
            return true;
        }
        return isSymmetricHelper(root.left,root.right);
        
        
    }
}