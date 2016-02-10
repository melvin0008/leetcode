public class Solution {
    public ArrayList<Integer> prevSmaller(ArrayList<Integer> arr) {
        Stack<Integer> st= new Stack<Integer>();
        ArrayList<Integer> min=new ArrayList<Integer>();
        for(int i=0;i<arr.size();i++){
            min.add(-1);
        }
        for(int i=0;i<arr.size();i++){
            while(!st.isEmpty()&& st.peek()>=arr.get(i))
                st.pop();
            if(!st.isEmpty())
                min.set(i,st.peek());
            st.push(arr.get(i));
        }
        return min;
    }
}
