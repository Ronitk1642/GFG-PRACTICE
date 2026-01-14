class Solution:
    def catchThieves(self, arr, k):
        from collections import Counter
        n= len(arr)
        
        c = 0
        thief = []
        police = []
        for i in range(n):
            if(arr[i] == "T"):
                thief.append(i)
            else:
                police.append(i)
        i = j = 0
        
        while i < len(police) and j < len(thief):
            if(abs(police[i] - thief[j]) <=k):
                c+=1
                i+=1
                j+=1
            elif police[i] < thief[j]:
                i+=1
            else:
                j+=1
            
        return c