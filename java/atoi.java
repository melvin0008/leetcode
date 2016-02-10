public class Solution {
	public int atoi(final String a) {
        String trimmedA=a.replaceAll("^\\s+", "");
        StringBuilder sb = new StringBuilder();
        int neg=1;
        if(trimmedA.charAt(0)=='-'){
            neg=-1;
        }
        trimmedA=trimmedA.replaceAll("^-|\\+","");
        for (int i=0;i<trimmedA.length();i++){
            char current=trimmedA.charAt(i);
            if(!Character.isDigit(current)) break;
            sb.append(current);
        }
        String numb=sb.toString();
        int base=0;
        int num=0;
        for(int i=numb.length()-1;i>=0;i--){
            
            num+=Character.getNumericValue(numb.charAt(i))*Math.pow(10,base);
            if(num>=Integer.MAX_VALUE){
                if(neg==1){
                    return neg*Integer.MAX_VALUE;
                }
                else{
                    return neg*Integer.MIN_VALUE;
                }
                    
            }
            base++;
        }
        return neg*num;
	}
}
