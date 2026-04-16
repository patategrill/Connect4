def empty_grid():
    """create the start grid"""
    return [[0 for _ in range(7)] for _ in range(6)]

def display_grid(grid):
    """define the display of the game grid
        like this :
         .  .  .  .  .  .  .
         .  .  .  .  .  .  .
         .  .  .  .  .  .  .
         .  .  .  .  .  .  .
         .  .  .  .  .  .  .
         .  .  .  .  .  .  .
    where . is an empty cell, x is the piece of player 1 and o is the piece of player 2"""
    for line in grid:
        for element in line:
            if element == 0:
                print(" . ", end="")
            elif element == 1:
                print(" x ", end="")
            elif element == 2:
                print(" o ", end="")
        print()

def possible_move(grid, col):
    """check if a move is possible in the given column"""
    return grid[0][col] == 0


def play(grid, n_player, col):
    for line in reversed(grid):
        if line[col] == 0:
            line[col] = n_player
            break
    return grid
"""function that places the player's piece in the chosen column"""

def horizontal(grid, n_player, line, col):
    for i in range(0,3):
        if grid[line][col+i] != n_player:
            return False
    return True
"""function that checks if there are 4 pieces aligned horizontally, if so it returns true"""

def vertical(grid, n_player, lig, col):
    if lig > 2:
        return False
    for i in range(4):
        if grid[lig+i][col] != n_player:
            return False
    return True


"""function that checks if there are 4 pieces aligned vertically, if so it returns true"""

def diag_top(grid, n_player, lig, col):
    for i in range(4):
        if grid[lig-i][col+i] != n_player:
            return False
    return True
"""function that checks if there are 4 pieces aligned diagonally upwards, if so it returns true"""

def diag_bottom(grid, n_player, lig, col):
    for  i in range(4):
        if grid[lig+i][col+i] != n_player:
            return False
    return True
"""function that checks if there are 4 pieces aligned diagonally downwards, if so it returns true"""

def victory(grid, n_player, lig, col):
    # vertical
    if vertical(grid, n_player, lig, col): # verify if there are 4 pieces aligned vertically, if so it returns true
        return True

    # horizontal
    for c in range(max(0, col-3), min(col+1, 4)): # verify the horizontal victory
        if horizontal(grid, n_player, lig, c):
            return True

    # diagonal bottom right
    for i in range(-3, 1): # loop to verify the bottom-right diagonal
        l = lig + i
        c = col + i
        if 0 <= l <= 2 and 0 <= c <= 3: # verify the grid boundaries
            if diag_bottom(grid, n_player, l, c): 
                return True

    # diagonal top right
    for i in range(-3, 1): # loop to verify the top-right diagonal
        l = lig - i 
        c = col + i
        if 3 <= l <= 5 and 0 <= c <= 3: # verify the grid boundaries
            if diag_top(grid, n_player, l, c):
                return True
    return False

"""Verify if any of the victory conditions is met, if so it's a win (true)"""
def draw(grid):
    for case in grid[0]:
        if case == 0 :
            return False
    return True
    
"""Verify if there is an empty cell in the grid, if so it's not a draw (false) otherwise it's a draw (true)"""
grid = empty_grid() # initialization of the grid
player = 1 # player 1 starts the game
end = False 

while not end: # main game loop
    display_grid(grid) # display the grid 

    col = int(input(f"Player {player}, choose a column (0 to 6) : ")) # ask the player to choose a column

    if col < 0 or col > 6: # verify that the column is valid
        print("Invalid column") # write a message to say that the column is invalid
        continue 

    if not possible_move(grid, col): # verify that the move is possible in the chosen column
        print("Column full") # write a message if the column is full
        continue 

    
    play(grid, player, col)# we play the move

    # search for the line where the piece was placed
    for lig in range(6): # browse the grid to find the line where the piece was placed
        if grid[lig][col] == player:  # if we find the piece of the player in the column, we save the line number and break the loop
            line = lig # we save the line number
            break 

    # victory 
    if victory(grid, player, line, col): # verify if the victory conditions are met
        display_grid(grid) # display the grid
        print(f"🎉 Player {player} has won!") 
        end = True

    # draw
    elif draw(grid): # verify if the draw conditions are met
        display_grid(grid) # display the grid
        print("🤝 Draw") 
        end = True

    # change player
    else:
        player = 2 if player == 1 else 1 # change player1 to player2 
