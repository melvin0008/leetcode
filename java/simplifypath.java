public class Solution {
    public String simplifyPath(String path) {
        Stack<String> cache= new Stack<String>();
        String[] arr= path.split("/");
        String sb = new String("");
        for(int i=1;i<arr.length;i++){
            if(arr[i].equals(".")){
                continue;
            }
            if(arr[i].equals("..")){
                if(!cache.isEmpty())
                    cache.pop();
            }
            else{
                if(!arr[i].isEmpty())
                    cache.push(arr[i]);
            }
        }
        if(cache.isEmpty()){
            return new String("/");
        }
        while(!cache.isEmpty()){
            sb="/"+cache.pop()+sb;
        }
        return sb;
    }
}