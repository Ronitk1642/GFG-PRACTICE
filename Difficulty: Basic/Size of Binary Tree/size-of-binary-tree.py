"""
Definition for Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""
class Solution:
    def getSize(self, root):
        # code here
        size = 0
        temp = root
        
        while temp != None:
            if temp.left == None:
                size += 1
                temp = temp.right
            else:
                left = temp.left
                
                while left.right != None and left.right != temp:
                    left = left.right
                
                if left.right == None:
                    size += 1
                    left.right = temp
                    temp = temp.left
                elif left.right == temp:
                    temp = temp.right
                    left.right = None
        
        
        return size
        