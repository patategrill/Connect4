#include <stdio.h>

int grid[6][7];
int i,j;

int empty_grid() {
    
    for (i=0;i<7;i++)
    {
        for (j=0;i<6;i++)
        {
            grid[i][j]=0;
        }
    }
}    

int display_grid() {
    for (i=0;i<7;i++) {
        for (j=0;j<6;j++){
            if (grid[i][j] == 0){
                printf(" . ");
            }
            else if (grid[i][j] == 1){
                printf(" x ");
            }
            else if(grid[i][j] == 2) {
                printf(" o ");
            }
        }
        
    }
    printf('\n');
}

int possible_move(col){
    return grid[0][col] == 0;
}

int play(n_player, col) {
    for (i=5;i>0;i--)
    {
        if (grid[col] == 0)
        {
            grid[col][i] = n_player;
            break;
        }
        return grid;
    }
    
}
