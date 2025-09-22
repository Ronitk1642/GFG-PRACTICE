class Solution:
    def maxOfMins(self, arr):
        # code here
        # nse and pse
        
        n=len(arr)
        def pse():
            st=[]
            lst=[-1 for _ in range(n)]
            for i in range(len(arr)):
                while st and arr[st[-1]]>arr[i]:
                  st.pop()
                if st:
                    lst[i]=st[-1]
                st.append(i)
            return lst
        def nse():
            st=[]
            lst=[n for _ in range(n)]
            for i in range(len(arr)-1,-1,-1):
                while st and arr[st[-1]]>=arr[i]:
                    st.pop()
                if st:
                    lst[i]=st[-1]
                st.append(i)
            return lst
        l1=pse()
        l2=nse()
        op=[0]*n
        best=[0]*n
        
        for i in range(len(l1)):
            v=l2[i]-l1[i]-1
            best[v-1]=max(best[v-1],arr[i])
        maxi=0
        
        for i in range(len(op)-1,-1,-1):
            maxi=max(maxi,best[i])
            op[i]=maxi
        return op

