class Solution {
  public:
  void solve(int i,int j,int n,vector<vector<int>>&mat,string &str,vector<string>&result){
      if(i<0 || j<0 || i>=n || j>=n || mat[i][j]==0)return;
      if(i==n-1 && j==n-1){
          result.push_back(str);
          return;
      }
      // backtrack and for avoid cycle 
      int cellVal=mat[i][j];
      mat[i][j]=0;
      
      //'D'(down)
      str.push_back('D');
      solve(i+1,j,n,mat,str,result);
      str.pop_back();
      
      //'L'(left),
      str.push_back('L');
      solve(i,j-1,n,mat,str,result);
      str.pop_back();
      
      //'R'(right)
      str.push_back('R');
      solve(i,j+1,n,mat,str,result);
      str.pop_back();
      
      //'U'(up),
      str.push_back('U'); //only push char 
      solve(i-1,j,n,mat,str,result);
      str.pop_back();
      
      mat[i][j]=cellVal;
  }
    vector<string> ratInMaze(vector<vector<int>>& maze) {
        // code here
        // Consider a rat placed at position (0, 0) in an n x n square matrix maze[][]. 
        //The rat's goal is to reach the destination at position (n-1, n-1). 
        //The rat can move in four possible directions: 'U'(up), 'D'(down), 'L' (left), 'R' (right).
        // 0: A blocked cell through which the rat cannot travel.
       // 1: A free cell that the rat can pass through.
    //   lexicographically smallest order. then 'D' 'L' 'R' 'U'
        int n=maze.size();
        vector<string>result;
        string str="";
        solve(0,0,n,maze,str,result);
        return result;
    }
};