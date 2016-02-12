public class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int prev=0;
        int i=0;
        int savei=0;
        int sumi=0;
        int min=Integer.MAX_VALUE;
        while(i<nums.length){
            sumi+=nums[i];
            while(sumi>=s){
                min=Math.min(min,i-savei+1);
                sumi-=nums[savei++];
            }
            i++;
        }
        return min==Integer.MAX_VALUE? 0:min ;
    }
}