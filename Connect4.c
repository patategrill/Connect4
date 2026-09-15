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

int horizontal(n_player, line, col) {
    for (i=0;i<4;i++)
    {
        if (grid[line][col+i])
        {
            return false;
        }
    return true;
    }
}

int vertical(n_player,lig,col) {
    if (lig > 2)
    {
        return false;
    }
    for (i=0;i<4;i++)
    {
        if (grid[lig+1][col] != n_player)
        {
            return false;
        }
    return true;
    }
}

int diag_top(n_player,lig,col){
    for (i=0;i<4;i++)
    {
        if (grid[lig-i][col+i] != n_player)
        {
            return false;
        }
        return true;
    }   
}

int diag_bottom(n_player,lig,col){
    for (i=0;i<4;i++)
    {
        if (grid[lig+i][col+i] != n_player)
        {
            return false;
        }
        return true;
    }   
}

int victory(n_player,lig,col){
    if (vertical(n_player,lig,col))
    {
        return true;
    }
    
    for (i=0;i<5; i++)/*Error here max in py doesnt exist*/
    {
        if horizontal(n_player,lig,c){
            return true;
        }
    }
    
}
