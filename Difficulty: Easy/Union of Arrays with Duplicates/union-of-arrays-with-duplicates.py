class Solution:    
    def findUnion(self, a, b):
        # code here
        for ele in b:
            a.append(ele)
        
        return list(dict.fromkeys(a))