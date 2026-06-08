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

# Delete function for 0 and 1 child 

def delete (root,value):
    if root == None:
        return root
    elif root.data > value :
        root.left = delete(root.left,value)
    elif root.data < value :
        root.right = delete(root.right,value)
    else:
        if root.right == None:
            return root.left
        elif root.left == None:
            return root.right
        # delete node when it has both child 
        else:
            successor = get_successor(root)
            # replce it with the current value
            root.data = successor.data
            # delete the successor
            root.right = delete(root.right,successor.data)
    # make sure to return root at end
    return root

# get inorder successor
def get_successor(root):
    root = root.right
    while root != None and root.left != None:
        root = root.left
    return root

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
root = insert(root,20)
root = insert(root,30)
root = insert(root,70)
root = insert(root,80)

# delete(root,100)


inOrder(root)

delete(root,75)
print("\n")
inOrder(root)

# search(root,100)