class Node:

    def __init__(self,x):

        self.data=x

        self.next=None

 



class Solution:

    def compute(self,head):

        # code here

        def rev(head):

            prev=None

            curr=head

            while(curr):

                next=curr.next

                curr.next=prev

                prev=curr

                curr=next

            return prev

            

        head1=rev(head)

        prev=head1

        curr=head1.next

        cm=head1.data

        while(curr):

            if curr.data<cm:

                prev.next=curr.next

                temp=prev.next

                del(temp)

                curr=curr.next

            else:

                cm=curr.data

                prev=curr

                curr=curr.next

        return rev(head1)

