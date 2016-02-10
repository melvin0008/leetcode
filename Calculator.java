import java.util.ArrayList;
import java.util.Arrays;
import java.util.EmptyStackException;
import java.util.Scanner;
import java.util.Stack;


//Class to evaluate Reverse Polish Notation
class Calculator{

	//Enum for operations
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

    //Function to validate input expression
	private ArrayList<String> validate(String input)
	{
		//Split Input Expression based on spaces
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
		            return new ArrayList<String>();
		        }   
		    }   
    	return	new ArrayList<String>(Arrays.asList(tokens));
	}
	//Function to evaluate expression with one operator
	private float calculate(String operator, float first , float second) throws IllegalArgumentException{
			if(operator.equals(Operations.ADD.value)) {
				return first + second;
	        }
	        else if (operator.equals(Operations.SUBTRACT.value)) {
	            return first-second;
	        } 
	        else if (operator.equals(Operations.MULTIPLY.value)) {
	            return first * second;
	        } 
	        else {
	        	
	        	float temp=first/second;
	        	return temp;
	        } 
	}

	public float evaluate(String input) throws IllegalArgumentException{
		//Validate Input to check for unvalid characters
		ArrayList<String> expList = this.validate(input);
		if(expList.size()==0) return Float.NaN;
		//Stack to evaluate postfix expression
		Stack<Float> nums= new Stack<Float>();
		float first;
		float second;
		for (String str : expList) {
			//If one of '+' '-' '*' or '/' pop two elements and evaluate
	        //If its a number push to stack
	        if (str.equals(Operations.ADD.value) || str.equals(Operations.SUBTRACT.value)|| str.equals(Operations.MULTIPLY.value)|| str.equals(Operations.DIVIDE.value)) {
	            try{
		            second = nums.pop();
		            first = nums.pop();
		            this.calculate(str, first, second);
	            }
	            catch(EmptyStackException e){
	            	System.out.println("Invalid Postfix Expression");
	            	return Float.NaN;
	            }
	            float ans=this.calculate(str,first,second);
	            nums.push(ans);
	        }else {

	            first = Integer.parseInt(str);
	            nums.push(first);
	        }
	        
	    }
	    //For the case if user inputs 5 3 and no operator
	    if(nums.size()==0 || nums.size()>1){
	    	System.out.println("Invalid Postfix Expression");
	        return Float.NaN;
	    } 
	    return nums.peek();
	}

	public static void main(String[] args) {

		//Create a Calculator object
        Calculator calc=new Calculator();
        while(true){
        	System.out.println("Enter your expression");
        	System.out.println("Type exit to quit");
        	Scanner in = new Scanner(System.in);
        	String input= in.nextLine();
        	if(input.equals("exit")) break;
        	//Call the evaluate function
        	float ret=calc.evaluate(input);
        	System.out.println("Answer is : "+ ret+"\n\n");
        	
        }
    }
}


/*
Testcases which I ran are:

5 3 + (Or any valid Postfix)

5 3   (Expression with more than one number and none operators)
5 + 3 (Or any variation of this)
a + b (Or any variation of letters and characters) 

*/