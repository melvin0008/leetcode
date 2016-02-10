public class Solution {
    private void getCombo(String digits, String[] phonelist, int curr,int n,String currResult,ArrayList<String>results){
        if(curr==n){
            if(currResult!=null &&currResult!=""){
                results.add(currResult);
            }
            return;
        }
        int c = Character.getNumericValue(digits.charAt(curr));
        for(int i=0;i<phonelist[c].length();i++){
            String temp=currResult+phonelist[c].charAt(i);
            getCombo(digits,phonelist,curr+1,n,temp,results);
        }
    }
    
    public List<String> letterCombinations(String digits) {
         String[] phonelist = {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
         ArrayList<String> results= new ArrayList<String>();
         this.getCombo(digits,phonelist,0,digits.length(),"",results);
         return results;
    }
}