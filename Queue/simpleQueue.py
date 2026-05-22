class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def insert(self , value):
        self.items.append(value)

    def delete(self):

        if self.isEmpty() :
            print("The queue is empty")
            return None
        else :
            return self.items.pop(0)


Q = Queue()

Q.insert(100)
Q.insert(200)
Q.insert(300)

print(Q.delete())

       

