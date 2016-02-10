public class Solution {
    public int[] plusOne(int[] digits) {
        int i=digits.length-1;
        while(i>=0 ){
            if(digits[i]==9){
                digits[i]=0;
            }
            else{
                digits[i]+=1;
                return digits;        
            }
            i--;
        }
        int[] ret= new int[digits.length+1];
        ret[0]=1;
        return ret;
    }
}