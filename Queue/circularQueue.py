class circularQueue:
    def __init__(self,size):
        self.size = size
        self.items = [None]*size
        self.front = self.rear = -1

    def enque(self,value):

        if ((self.rear + 1)%self.size == self.front):
            print(" the Queue is full")

        elif( self.front == -1):
            self.front = self.rear = 0
            self.items[self.rear]=value

        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value
            return None
    def deque(self):
        if (self.front == -1):
            print("Queue is Empty")
        elif (self.front == self.rear):
            print(self.items[self.front])
            self.front = self.rear = -1
        else:
            print(self.items[self.front])
            self.front = (self.front + 1) % self.size


c = circularQueue(5)

c.enque(10)
c.enque(20)
c.enque(30)
c.enque(40)
c.enque(50)

c.deque()

c.enque(60)

c.enque(70)