public class Solution {
    public int search(int[] nums, int target) {
        int low=0;
        int high=nums.length-1;
        int mid;
        while(low<=high){
            mid=(low+high)/2;
            if(nums[mid]==target){
                return mid;
            }
            else if(nums[mid]>nums[low]){
                if(nums[mid]>target&&target>=nums[low]){
                    high=mid-1;
                }
                else{
                    low=mid+1;
                }
            }
            else if(low==mid){
                low++;
            }
            else if(nums[mid]<nums[high]){
                if(nums[mid]<target&&target<=nums[high]){
                    low=mid+1;
                }
                else{
                    high=mid-1;
                }
            }
            else if(high==mid){
                high--;
            }
            
        }
        return -1;
        
    }
}