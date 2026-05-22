class Stack:
    def __init__(self):
        self.stk = []

    def push(self,value):
        self.stk.append(value)

    def peek(self):
        if(len(self.stk)==0):
            raise Exception("The stack is full")
        last = int(len(self.stk)-1)
        return self.stk[last]
    
    def pop(self):
        if(len(self.stk)==0):
            raise Exception("The stack is full")
        self.stk.pop()

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.pop()
print(stack.peek())