class Solution {
    public int uniquePaths(int m, int n) {
        // defining a dp matrix and intializing all cells as -1;
        int dp[][] = new int[m][n];
        for(int i=0; i<dp.length;i++){
            for(int j=0;j<dp[0].length;j++){
                dp[i][j]=-1;
            }
        }
        return result(0,0,m,n, dp);
    }

    static int result(int row, int col, int m, int n, int[][] dp){

        //return 1 if we reach the end of the array
        if(row==m-1 && col==n-1){
            return 1;
        }

        //return the cell value if we already have traveresed it
        if(dp[row][col]!=-1){
            return dp[row][col];
        }

        //memoization: If the path has not been traversed yet
        if(row == m-1){
            return dp[row][col]=result(row, col+1, m, n, dp);
        }else if(col == n-1){
           return dp[row][col]=result(row+1, col, m, n, dp);
        }

        return dp[row][col]=result(row+1, col, m, n, dp)+result(row, col+1, m, n, dp);
    }
}