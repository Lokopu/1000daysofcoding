import numpy as np



def main():
    # Initialize tictactoe grid of NaN values
    grid = np.full((3,3), np.nan)
    players = []
    for player in range(2):
        players.append(input(f"Please input name of player {player+1}: "))
    
    round = 1


    while check_winner(grid) == False:
        print()
        print("Current situation:")
        print(grid)
        # Print additional line
        print()
        
        # Initialize players
        if round % 2 != 0: 
            current_player = players[0]
        else:
            current_player = players[1]
        print(f"{current_player}, your turn...")
        x, y = input("Please input your desired placement 'row, column'/'3, 2': ").split(",")
        x = int(x.strip(", '"))
        y = int(y.strip(", '"))
        updated_grid, success  = insert_tile(players, current_player, x, y, grid)
        if success == False:
            continue
        else:     
            round += 1
        
        if check_winner(grid) in [1, 2]:
            print(f"{current_player} WON!")


def insert_tile(players, player, x, y, grid):
    success = False
    # Initialize if the given player is playing as "0" or as "1" in the grid.
    tile = players.index(player) + 1 
    
    # Add zero indexing to human input
    x -= 1
    y -= 1

    if 0 <= x <= 2 or 0 <= y <= 2:
        # Assign that players tile to the chosen location on grid
        if np.isnan(grid[x,y]) == True:
            grid[x][y] = tile
            success = True
        else:
            print("!!! - Placement already taken, please try another location")
    else: 
        print("!!! - Can't place tile there")
        
    return grid, success


def check_winner(grid): ## I Am missing implementation of diagonal way to win        
    check = False
    if np.sum(grid) == np.nan:
        return check
    
    row_sums = np.sum(grid, axis=0)
    
    column_sums = np.sum(grid, axis=1)

    for i in range(2):
        # Check if player one wins by having 3 ones in a row/column
        if row_sums[i] == 3 or column_sums[i] == 3:
            winner = 1
            return winner
        # Check if player one wins by having 3 twos in a row/column
        elif row_sums[i] == 6 or column_sums[i] == 6:
            winner = 2
            return winner
    
    # If loop exits without a winner return False
    return check
        


if __name__ == "__main__":
    main()