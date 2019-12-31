#Program to find the Height of any given Binary Search Tree
'''
Logic:
Here I've taken 1 result array and I'm adding the level value of each Leaf node. After getting the level values of all the Leaf nodes,
I'm returning the value of level of the Farthest Leaf node
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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def preOrder(root, prev_level, result_set):
    current_node = root
    left_node = root.left
    right_node = root.right
    
    current_node.level = prev_level + 1

    if left_node!=None:
        preOrder(left_node,current_node.level,result_set)

    if right_node!=None:
        preOrder(right_node, current_node.level,result_set)

    #print("Node: "+str(current_node.info)+" Level: "+str(current_node.level))

    if current_node.left == None and current_node.right == None:
        result_set.append(current_node.level)
    

def height(root):
    root.level = 0
    result = []
    preOrder(root, 0, result)
    return max(result)-1


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
