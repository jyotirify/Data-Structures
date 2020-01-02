'''
LOGIC:
This is similar to BFS Traversal in Graphs. Here, we are using a Queue to travel all the nodes level wise.
We insert the root node in the Queue first, then we pop it and insert all it's children (first left then right) 
until we visit all the nodes.
'''

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

def traverseBST(queue):
    if len(queue)!=0:
        ele = queue.pop(0)
        if ele!=None:
            queue.append(ele.left)
            queue.append(ele.right)
            print(ele,end = " ")
        traverseBST(queue)
    else:
        return
    
def levelOrder(root):
    #Write your code here
    queue = []
    queue.append(root)
    traverseBST(queue)

    



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)
