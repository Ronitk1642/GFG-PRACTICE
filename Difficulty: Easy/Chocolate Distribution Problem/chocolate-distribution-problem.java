class Solution {
    public int findMinDiff(ArrayList<Integer> arr, int m) 
    {
        // your code here
        int ans= Integer.MAX_VALUE;
        int n= arr.size();
        Collections.sort(arr);
        for(int x=0;x<=n-m; x++)
        {
            ans= Math.min(ans, arr.get(x+m-1)-arr.get(x));
        }
        
        
        return ans;
    }
}