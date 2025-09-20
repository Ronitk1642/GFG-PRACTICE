class Solution {
  public:
    int longestSubarray(vector<int>& arr) {
        int n=arr.size();
        stack<int> st;
        vector<int> ngei(n,n);
        for(int i=n-1;i>=0;i--){
            while(!st.empty() && arr[st.top()]<=arr[i]) st.pop();
            if(!st.empty()) ngei[i]=st.top();
            st.push(i);
        }
        while(!st.empty()) st.pop();
        int ans=0;
        for(int i=0;i<n;i++){
            int pgei=-1;
            while(!st.empty() && arr[st.top()]<=arr[i]) st.pop();
            if(!st.empty()) pgei=st.top();
            st.push(i);
            int subarraylen=ngei[i]-pgei-1;
            if(subarraylen>=arr[i]) ans=max(ans,subarraylen);
        }
        return ans;
    }
};