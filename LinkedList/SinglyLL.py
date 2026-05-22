class Node :
    def __init__(self,info,next=None):
        self.data = info
        self.next = next


# visualize to learn and understand it 
class SinglyLL :
    def __init__(self,head=None):
        self.head = head

    def insertAtEnd (self , value) :
        temp = Node(value)
        if(self.head != None) :
            # t1 is only traversing only
            t1 = self.head
            while(t1.next != None) :
                t1 = t1.next
            t1.next = temp
        else :
            self.head = temp

    def insertAtFront(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insertAtMid(self,value,x):
        temp = Node(value)
        t1 = self.head
        while(t1.next != None):
            if(t1.data == x):
                temp.next = t1.next
                t1.next = temp
            
            t1 = t1.next

    def deleteLL(self,value):
        t1 = self.head
        prev = t1
# for the first node
        if(t1.data == value):
            self.head = t1.next

# for the middle nodes
        while (t1.next != None):
            if(t1.data == value):
                prev.next = t1.next
                break
            else:
                prev = t1
                t1=t1.next
# for the last node
        if(t1.data ==value):
            prev.next = None


    
    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)

obj = SinglyLL()

obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtMid(100,10)
obj.deleteLL(30)
obj.printLL()
