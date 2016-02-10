public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ret= new ArrayList<List<Integer>>();
        Arrays.sort(nums);
        int curr,j,k,temp;
        for(int i=0;i<nums.length;i++){
            if (nums[i]>0) break;
            if (i>0 && nums[i]==nums[i-1]) continue;
            curr=nums[i];
            j=i+1;
            k=nums.length-1;
            while(j<k){               
                temp=curr+nums[j]+nums[k];
                if(temp==0){
                    ret.add(Arrays.asList(curr,nums[j],nums[k]));
                    while(j<k && nums[j]==nums[j+1]) j++;
                    j++;
                    while(j<k && nums[k]==nums[k-1]) k--;
                    k--;
                }
                else if(temp>0){
                    while(j<k && nums[k]==nums[k-1]) k--;
                    k--;
                }
                else{
                    while(j<k && nums[j]==nums[j+1]) j++;
                    j++;
                }
            }
        }
        return ret;
        
    }
}