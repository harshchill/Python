class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value

def insert(root,value):
    if(root == None):
        return Node(value)
    if(root.data == value):
        return root
    if(root.data > value):
        # for this to work make sure the funtion should return the address of the root( root can be a node dont stick to root word)
        # address is assigned to root.left 
        root.left = insert(root.left,value)
    else:
        root.right = insert(root.right,value)
    # this return the root address
    return root

def search(root,value):
    if(root == None):
        print(f"{value} not found")
        return 
    if(root.data == value):
        print(f"{value} found")
        return 
    if(root.data > value):
        search(root.left,value)
    else:
        search(root.right,value)

# for traversal
def inOrder(root):
    if(root != None):
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)
        return


# making a tree
# root are assigned again for defensive habit
root = insert(None,50)
root = insert(root,75)
root = insert(root,25)
root = insert(root,10)
root = insert(root,35)
root = insert(root,60)
root = insert(root,100)

inOrder(root)

search()