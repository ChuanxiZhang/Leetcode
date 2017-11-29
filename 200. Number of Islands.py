class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for (int i = 0; i<grid.length;i++){
            for(int j = 0; j<grid[i].length;j++){
                if (grid[i][j]=='1'){
                    count++;
                    DFS(grid,i,j);
                }
            }
        }
        return count;
    }
    public void DFS(char [][] grid, int x, int y){
        if(x < 0||y < 0|| x>=grid.length||y>=grid[0].length||grid[x][y]!='1') return;
        grid[x][y]='0';
        DFS(grid,x-1,y);
        DFS(grid,x,y-1);
        DFS(grid,x+1,y);
        DFS(grid,x,y+1);

    }
}
