class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLL :
    def __init__(self):
        self.head = None

    def insertAtEnd(self,value):

        temp = Node(value)
        
        if(self.head == None):
            self.head=temp
            return
        
        t = self.head
        while(t.next != None):
            t = t.next
        t.next = temp
        temp.prev = t

    def insertAtBeg(self,value):
        temp = Node(value)
        t = self.head
        if(t == None):
            self.head=temp
            return
        temp.next = t 
        t.prev= temp
        self.head = temp

    def insertAtMid(self,value,x):
        temp = Node(value)
        if(self.head == None):
            self.head=temp
            return
        t = self.head
        while(t.data != x):
            t = t.next
        t1 = t.next 
        t.next = temp
        temp.prev = t
        if(t1 != None):
            t1.prev = temp

        temp.next = t1

    def deleteLL (self , value):
        temp = self.head
        front = temp.next
        last = temp.prev
        if(temp.data == value):
            front.prev = None
            self.head = front
            return

        while (temp.data != value):
            last = temp 
            temp = temp.next
            front = temp.next
            
        if(temp.data == value):
            last.next = front
            if(front != None):
                front.prev= last

            


    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data , end=" <-> ")
            t1 = t1.next
        print(t1.data)

    
obj = DoublyLL()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtBeg(1)
obj.insertAtMid(35,30)
obj.insertAtMid(45,40)
obj.deleteLL(30)
obj.printLL()

