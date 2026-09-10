def empty_grid():
    """create the start grid"""
    return [[0 for _ in range(3)] for _ in range(3)]

def display_grid(grid):
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
    return grid[0][col] == 0   

def play(grid, n_player, col):
    for line in reversed(grid):
        if line[col] == 0:
            line[col] = n_player
            break
    return grid     

def horizontal(grid, n_player, line, col):
    for i in range(0,2):
        if grid[line][col+i] != n_player:
            return False
    return True

def vertical(grid, n_player, lig, col):
    if lig > 2:
        return False
    for i in range(3):
        print("lig =", lig)
        print("i =", i)
        print("lig+i =", lig+i)
        print("nombre de lignes =", len(grid))
        if grid[lig][col] != n_player:
            return False
    return True

def diag_top(grid, n_player, lig, col):
    for i in range(3):
        if grid[lig-i][col+i] != n_player:
            return False
    return True    

def diag_bottom(grid, n_player, lig, col):
    for  i in range(3):
        if grid[lig+i][col+i] != n_player:
            return False
    return True

def victory(grid, n_player, lig, col):
    # vertical
    if vertical(grid, n_player, lig, col):
        return True

    # horizontal
    for c in range(max(0, col-2), min(col+1, 3)):
        if horizontal(grid, n_player, lig, c):
            return True

    # diagonal bottom right
    for i in range(-1, 1):
        l = lig + i
        c = col + i
        if 0 <= l <= 2 and 0 <= c <= 3:
            if diag_bottom(grid, n_player, l, c): 
                return True

    # diagonal top right
    for i in range(-1, 1):
        l = lig - i 
        c = col + i
        if 3 <= l <= 5 and 0 <= c <= 3:
            if diag_top(grid, n_player, l, c):
                return True
    return False

def draw(grid):
    for case in grid[0]:
        if case == 0 :
            return False
    return True

grid = empty_grid()
player = 1
end = False



while not end:
    display_grid(grid)

    col = int(input(f"Player {player}, choose a column (0 to 2) : "))

    if col < 0 or col > 2:
            print("Invalid column")
            continue 

    if not possible_move(grid, col):
            print("Column full")
            continue 

    play(grid, player, col)

    for lig in range(3):
            if grid[lig][col] == player:  
                line = lig
                break 

    print("lig =", lig)
    print("nombre de lignes =", len(grid))

    if victory(grid, player, line, col): 
            display_grid(grid)
            print(f" Player {player} has won!") 
            end = True

    elif draw(grid):
            display_grid(grid)
            print("🤝 Draw") 
            end = True

    else:
            player = 2 if player == 1 else 1
