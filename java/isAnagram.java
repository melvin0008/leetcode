public class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }
        int[] stringS=new int[256];
        for(int i=0;i<s.length();i++){
            stringS[s.charAt(i)]++;
        }
        for(int i=0;i<s.length();i++){
            
            if(--stringS[t.charAt(i)]<0){
                return false;
            };
        }
        for(int i=0;i<s.length();i++){
            
            if(stringS[s.charAt(i)]>0){
                return false;
            };
        }
        return true;
    }
}