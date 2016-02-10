public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> cache= new HashMap<Integer,Integer>();
        int [] ret= new int[2];
        for(int i=0; i<nums.length;i++ ){
            if(cache.containsKey(target-nums[i])){
                ret[0]=cache.get(target-nums[i])+1;
                ret[1]=i+1;
                return ret;
            } 
            else{
                cache.put(nums[i],i);
            }
        }   
        return ret;
    }
}