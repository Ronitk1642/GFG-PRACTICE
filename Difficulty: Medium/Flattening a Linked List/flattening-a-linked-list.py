class Solution:

    def flatten(self, root):

        if not root or not root.next:

            return root

        

        # Flatten the next nodes

        root.next = self.flatten(root.next)

        

        # Merge current bottom list with flattened next list

        root = self.merge(root, root.next)

        

        return root

 

    def merge(self, a, b):

        dummy = Node(0)

        temp = dummy

 

        while a and b:

            if a.data < b.data:

                temp.bottom = a

                a = a.bottom

            else:

                temp.bottom = b

                b = b.bottom

            temp = temp.bottom

 

        if a:

            temp.bottom = a

        if b:

            temp.bottom = b

 

        return dummy.bottom