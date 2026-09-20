#include <stdio.h>

int grid[6][7];
int i,j;

void empty_grid() {
    for (i=0;i<6;i++)
    {
        for (j=0;j<7;i++)
        {
            grid[i][j]=0;
        }
    }
}    

void display_grid() {
    for (i=0;i<6;i++) {
        for (j=0;j<7;j++){
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
        if (horizontal(n_player,lig,col)){
            return true;
        }
    }
    
    for (i=-3;i<1;i++)
    {
        int l=lig+i;
        int c=col+i;
        if (0 <= l <= 2 & 0 <= c <= 3)
        {
            if (diag_bottom(n_player,l,c))
            {
                return true;
            }
            
        }
        
    }
    
    for (i=-3;i<1;i++)
    {
        int l=lig-i;
        int c=col+i;

        if (3 <= l <= 5 & 0 <= c <= 3)
        {
            if (diag_top(n_player,l,c))
            {
                return true;
            }
            
        }
        return false;
    }
    
}

int draw(){
    for (i=0;i<7;i++)
    {
        if (grid[0][i]==0)
        {
            return false;
        }
    }
    return true;
}

int player=1;
bool end=false;
int col;

int main(){
    while (!end)
    {
        display_grid();

        printf('Player %d, choose a column (0 to 6) : ' ,player);
        scanf("%d",&col);
    }
}

