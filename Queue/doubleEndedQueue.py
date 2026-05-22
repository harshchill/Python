class dequeue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def insertAtFront(self,value):
        self.items.insert(0,value)
        return None
    
    def deleteAtFront(self):
        if self.isEmpty() :
            raise("The Queue is empty")
        else:
            return self.items.pop(0)
        
    def insertAtEnd(self,val):
        self.items.append(val)
        return None
    
    def deleteAtEnd(self):
        if self.isEmpty() :
            raise("The Queue is empty")
        else:
            return self.items.pop()
        
q = dequeue()

q.insertAtFront(10)
q.insertAtFront(20)
q.insertAtFront(30)
q.insertAtEnd(40)

print(q.deleteAtFront())
print(q.deleteAtEnd())