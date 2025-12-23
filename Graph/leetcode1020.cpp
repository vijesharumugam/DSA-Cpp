//  number of enclaves

class Solution {
public:
    
    void dfs(int i,int j,vector<vector<int>>& grid){
        grid[i][j] = 2;
        int n = grid.size();
        int m = grid[0].size();
        vector<pair<int,int>> dirc = {{0,1},{1,0},{-1,0},{0,-1}};
        for(auto& [x,y]:dirc){
            int xa = x + i;
            int yb = y + j;
            if(xa >= 0 && xa < n && yb >=0 && yb < m && grid[xa][yb] == 1){
                dfs(xa,yb,grid);
            }
        }
    }
    int numEnclaves(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size(); 
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (grid[i][0] == 1)
                dfs(i,0,grid);
            if (grid[i][m-1] == 1 )
                dfs(i,m-1,grid);
        }

        for (int j = 0; j < m; j++) {
            if (grid[0][j] == 1 )
                dfs(0,j,grid);
            if (grid[n-1][j] == 1)
                dfs(n-1,j,grid);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1)
                    ans++;
            }
        }
        return ans;
    }
};