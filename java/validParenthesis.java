public class Solution {
    public boolean isValid(String s) throws RuntimeException{
        Stack<Character> st = new Stack<Character>();
        for(int i=0;i<s.length();i++){
            char current=s.charAt(i);
            if(current=='(' || current=='{'|| current=='['){
                st.push(current);
            }
            else{
                if (st.isEmpty()) return false;
                char c = st.pop();
                if(c=='{' && current=='}'){
                    continue;
                }
                else if(c=='(' && current==')'){
                    continue;
                }
                if(c=='[' && current==']'){
                    continue;
                }
                
                return false; 
            }
        }
        
        if(!st.isEmpty()){
            return false;
        }
        return true;
    }
}