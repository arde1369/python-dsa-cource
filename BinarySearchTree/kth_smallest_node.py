class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    # WRITE KTH_SMALLEST METHOD HERE #
    #                                #
    #                                #
    #                                #
    #                                #
    #################################
 
    def kth_smallest(self, k):
        # create a stack to hold nodes
        stack = []    
        # start at the root of the tree      
        temp = self.root    
        
        while stack or temp:
            # traverse to the leftmost node
            while temp: 
                # add the node to the stack                
                stack.append(temp)      
                temp = temp.left
            
            # pop the last node added to the stack
            temp = stack.pop()           
            k -= 1
            # if kth smallest element is found, return the value
            if k == 0:                  
                return temp.value
            
            # move to the right child of the node
            temp = temp.right           
            
        # if k is greater than the number of nodes in the tree, return None
        return None

bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print(bst.kth_smallest(1))  # Expected output: 2
print(bst.kth_smallest(3))  # Expected output: 4
print(bst.kth_smallest(6))  # Expected output: 7


"""
    EXPECTED OUTPUT:
    ----------------
    2
    4
    7

 """