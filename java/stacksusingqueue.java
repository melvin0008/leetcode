class MyStack {
    private Queue<Integer> qa=new LinkedList<Integer>();
    private Queue<Integer> qb=new LinkedList<Integer>();
    
    // Push element x onto stack.
    public void push(int x) {
        if(qa.isEmpty()){
            qa.add(x);
            while(!qb.isEmpty())
                qa.add(qb.poll());
        }else{
            qb.add(x);
            while(!qa.isEmpty())
                qb.add(qa.poll());
        } 
    }

    // Removes the element on top of the stack.
    public void pop() {
        if(qa.isEmpty()){
          qb.remove();  
        }
        else{
            qa.remove();
        }
    }

    // Get the top element.
    public int top() {
        return qa.isEmpty() ? qb.peek() : qa.peek();
    }

    // Return whether the stack is empty.
    public boolean empty() {
        return qa.isEmpty() && qb.isEmpty();
    }
}