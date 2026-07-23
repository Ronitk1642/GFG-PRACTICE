'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
# Morris Pre-order Traversal

class Solution:
    def preOrder(self, root):
        
        curr = root
        res = []
        
        while curr != None:
            
            if curr.left:
                
                pred = curr.left
                while pred.right != None and pred.right != curr:
                    pred = pred.right
                    
                if pred.right is None:
                    res.append(curr.data)
                    pred.right = curr
                    curr = curr.left
                
                else:
                    pred.right = None
                    curr = curr.right
            
            else:
                res.append(curr.data)
                curr = curr.right
                
                
        return res