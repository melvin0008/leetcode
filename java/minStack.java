class MinStack {
    private ArrayList<Integer> stack;
    private ArrayList<Integer> minStack;
    
    public MinStack(){
        stack = new ArrayList<Integer> ();
        minStack = new ArrayList<Integer> ();
    }
    
    public void push(int x) {
        stack.add(x);
        if(minStack.isEmpty() || x<=this.getMin()){
            minStack.add(x);
        }
    }

    public void pop() throws RuntimeException {
        if(stack.isEmpty()) throw new RuntimeException();
        if(!minStack.isEmpty() && this.top()==this.getMin()){
            minStack.remove(minStack.size()-1);
        }
        stack.remove(stack.size()-1);
    }

    public int top() {
        return stack.get(stack.size()-1);
    }

    public int getMin() {
        return minStack.get(minStack.size()-1);
    }
}
