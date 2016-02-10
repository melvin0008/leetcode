import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

class Calculator{
	
	ArrayList<String> expList;

	 public enum Operations {
        ADD("+"),
        SUBTRACT("-"),
        MULTIPLY("*"),
        DIVIDE("/");
        private String value;
        Operations(String s) {
            this.value = s;
        }   
        String value() {
            return this.value;
        }   
    }   

	public Calculator(String input){
    	String [] tokens = input.split(" ");
		
		outer:  
		    for(String str:tokens) {
		        for(Operations op :Operations.values())
		            if(str.equals(op.value))
		                continue outer;    

		        try {
		            Float.parseFloat(str);
		        }   
		        catch (NumberFormatException n) {
		            System.out.println("Wrong input format");
		            return;
		        }   
		    }   

    	expList= new ArrayList<String>(Arrays.asList(tokens));	
	}

	private float calculate(char operator, float first , float second) throws IllegalArgumentException{
			if(operator=='+') {
				return first + second;
	        }
	        else if (operator=='-') {
	            return first-second;
	        } 
	        else if (operator=='*') {
	            return first * second;
	        } 
	        else {
	        	if(second==0){
	        		throw new IllegalArgumentException("Argument 'divisor' is 0");
	        	}
	        	return first/second;
	        } 
	}

	public float evaluate() throws IllegalArgumentException{
		Stack<Float> nums= new Stack<Float>();
		float first;
		float second;
		for (String str : this.expList) {
	        if (str.equals("+") || str.equals("-")|| str.equals("*")|| str.equals("/")) {
	            if(nums.isEmpty()) throw new IllegalArgumentException("Incorrect String Format");
	            second = nums.pop();
	            if(nums.isEmpty()) throw new IllegalArgumentException("Incorrect String Format");
	            first = nums.pop();
	            float ans=this.calculate(str.charAt(0),first,second);
	            nums.push(ans);
	        }else {
	            first = Integer.parseInt(str);
	            nums.push(first);
	        }
	        
	    }
	    
	    return nums.peek();
	}

	public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Calculator calc=new Calculator(in.nextLine());
        System.out.println(calc.evaluate());
      
    }
}