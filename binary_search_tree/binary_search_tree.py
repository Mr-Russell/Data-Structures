"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value < Node's value
        if value < self.value:
            # we need to go left 
            # if we see that there is no left child, 
            if self.left is None:
                # then we can wrap the value in a BSTNode and park it
                self.left = BSTNode(value)
            # otherwise there is a child 
            else:
                # call the left child's `insert` method 
                self.left.insert(value)
        # otherwise, value >= Node's value 
        else:
            # we need to go right 
            # if we see there is no right child, 
            if self.right is None:
                # then we can wrap the value in a BSTNode and park it 
                self.right = BSTNode(value)
            # otherwise there is a child 
            else:
                # call the right child's `insert` method 
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target is self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            node.right.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        current = [node]

        while len(current) > 0:
            next_level = []
            for item in current:
                print(item.value)
                if item.left is not None:
                    next_level.append(item.left)
                if item.right is not None:
                    next_level.append(item.right)
            
            current = next_level
                
        
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        items = [node]

        while len(items) > 0:
            current = items.pop()
            print(current.value)

            if current.left:
                items.append(current.left)
            if current.right:
                items.append(current.right)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
