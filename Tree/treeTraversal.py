class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value

def preOrder(root):
    if(root != None):
        print(root.data,end=" ")
        preOrder(root.left)
        preOrder(root.right)
   
    
def inOrder(root):
    if(root != None):
        
        preOrder(root.left)
        print(root.data,end=" ")
        preOrder(root.right)
   

def postOrder(root):
    if(root != None):
        
        preOrder(root.left)
        preOrder(root.right)
        print(root.data,end=" ")
   

root = Node(3)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(6)
root.left.right = Node(7)
root.right.left =Node(8)
root.right.right =Node(9)

preOrder(root)
print("Next")
inOrder(root)
print("Next")
postOrder(root)
