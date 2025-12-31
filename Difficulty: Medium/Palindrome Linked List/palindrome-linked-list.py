class Solution:
    def isPalindrome(self, head):
        result = []
        
        while head:
            result.append(head.data)
            head = head.next
        
        return result==result[::-1]