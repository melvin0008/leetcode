public class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character,Integer> cache=new HashMap<Character,Integer>();
        int left=-1;
        int max=0;
        for(int i=0;i<s.length();i++){
            char c =s.charAt(i);
            if (cache.containsKey(c) && cache.get(c) > left){
               left=cache.get(c); 
            }
            max=Math.max(max,i-left);
            cache.put(c,i);
        }
        return max;
    }
}