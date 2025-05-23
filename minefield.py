import random

MINEFIELD_ROWS = 10
MINEFIELD_COLUMNS = 10

"""
Create matrix (list of lists) and fill it by "0"
recipe: https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array
"""
minefieldArray = [[0 for c in range(MINEFIELD_COLUMNS+2)] for r in range(MINEFIELD_ROWS+2)]

"""
Our idealogy:
(-1) - mine in the cell
(+10) - cell is opened
(+100) - minesweeper in the cell
(0..8) - number mines in the the neighboring cells
"""

"""
Fill Minefield with new values.
"""
def fill_Minefield(mineNumber: int) -> bool:

    # Fill all minefieldArray by "0"
    for r in range(0, MINEFIELD_ROWS+2):
        for c in range(0, MINEFIELD_COLUMNS+2):
            minefieldArray[r][c] = 0

    # Fill minefieldArray by mines (set -1). Put mineNumber mines.
    m = 0
    while m <= mineNumber:
        r = random.randint(1, MINEFIELD_ROWS)
        c = random.randint(1, MINEFIELD_COLUMNS)
        # Don't put mine in first and last corners
        if ((r != 1 and c !=1) or (r != MINEFIELD_ROWS and c !=MINEFIELD_COLUMNS)):
            minefieldArray[r][c] = -1
            m +=1

    # Calculate mines around the cell
    for r in range(1, MINEFIELD_ROWS+1):
        for c in range(1, MINEFIELD_COLUMNS+1):
            n = 0
            if (minefieldArray[r][c] != -1):
                if (minefieldArray[r-1][c-1] == -1): n+=1
                if (minefieldArray[r-1][c] == -1): n+=1
                if (minefieldArray[r-1][c+1] == -1): n+=1
                if (minefieldArray[r][c+1] == -1): n+=1
                if (minefieldArray[r+1][c+1] == -1): n+=1
                if (minefieldArray[r+1][c] == -1): n+=1
                if (minefieldArray[r+1][c-1] == -1): n+=1
                if (minefieldArray[r][c-1] == -1): n+=1
                minefieldArray[r][c] = n

    # Open first corner and put minesweeper to it
    minefieldArray[1][1] = 110
    # Open last corner
    minefieldArray[MINEFIELD_ROWS][MINEFIELD_COLUMNS] = 10

    return True

"""
Do one step at the Minefield.
Minesweeper can step only to the neighboring cells.
Minesweeper will open this cell if it was closed.
Minesweeper will blow up if mine was in this cell.
Function returns true if we don't blow up
"""
def do_Step_Minefield(toRow: int, toColumn: int) -> bool:

    # We are stepping to this cell
    r = toRow
    c = toColumn

    # If we are in the the neighboring cells, then we do a step

    if (minefieldArray[r-1][c-1] >= 100):
        minefieldArray[r-1][c-1] -= 100   # leave the previous cell
        if (minefieldArray[r][c] >= 10):
            minefieldArray[r][c] += 100   # Put Minesweeper to this cell
        elif (minefieldArray[r][c] >= 0):
            minefieldArray[r][c] += 110   # Put Minesweeper to this cell and open this cell
        elif (minefieldArray[r][c] == -1):
            return False                  # Blow up!!!

    if (minefieldArray[r-1][c] >= 100):
        minefieldArray[r-1][c] -= 100   # leave the previous cell
        if (minefieldArray[r][c] >= 10):
            minefieldArray[r][c] += 100   # Put Minesweeper to this cell
        elif (minefieldArray[r][c] >= 0):
            minefieldArray[r][c] += 110   # Put Minesweeper to this cell and open this cell
        elif (minefieldArray[r][c] == -1):
            return False                  # Blow up!!!

    if (minefieldArray[r-1][c+1] >= 100):
        minefieldArray[r-1][c+1] -= 100   # leave the previous cell
        if (minefieldArray[r][c] >= 10):
            minefieldArray[r][c] += 100   # Put Minesweeper to this cell
        elif (minefieldArray[r][c] >= 0):
            minefieldArray[r][c] += 110   # Put Minesweeper to this cell and open this cell
        elif (minefieldArray[r][c] == -1):
            return False                  # Blow up!!!

    if (minefieldArray[r][c+1] >= 100):
        minefieldArray[r][c+1] -= 100   # leave the previous cell
        if (minefieldArray[r][c] >= 10):
            minefieldArray[r][c] += 100   # Put Minesweeper to this cell
        elif (minefieldArray[r][c] >= 0):
            minefieldArray[r][c] += 110   # Put Minesweeper to this cell and open this cell
        elif (minefieldArray[r][c] == -1):
            return False                  # Blow up!!!

    if (minefieldArray[r+1][c+1] >= 100):
        minefieldArray[r+1][c+1] -= 100   # leave the previous cell
        if (minefieldArray[r][c] >= 10):
            minefieldArray[r][c] += 100   # Put Minesweeper to this cell
        elif (minefieldArray[r][c] >= 0):
            minefieldArray[r][c] += 110   # Put Minesweeper to this cell and open this cell
        elif (minefieldArray[r][c] == -1):
            return False                  # Blow up!!!

    if (minefieldArray[r+1][c] >= 100):
        minefieldArray[r+1][c] -= 100   # leave the previous cell
        if (minefieldArray[r][c] >= 10):
            minefieldArray[r][c] += 100   # Put Minesweeper to this cell
        elif (minefieldArray[r][c] >= 0):
            minefieldArray[r][c] += 110   # Put Minesweeper to this cell and open this cell
        elif (minefieldArray[r][c] == -1):
            return False                  # Blow up!!!

    if (minefieldArray[r+1][c-1] >= 100):
        minefieldArray[r+1][c-1] -= 100   # leave the previous cell
        if (minefieldArray[r][c] >= 10):
            minefieldArray[r][c] += 100   # Put Minesweeper to this cell
        elif (minefieldArray[r][c] >= 0):
            minefieldArray[r][c] += 110   # Put Minesweeper to this cell and open this cell
        elif (minefieldArray[r][c] == -1):
            return False                  # Blow up!!!

    if (minefieldArray[r][c-1] >= 100):
        minefieldArray[r][c-1] -= 100   # leave the previous cell
        if (minefieldArray[r][c] >= 10):
            minefieldArray[r][c] += 100   # Put Minesweeper to this cell
        elif (minefieldArray[r][c] >= 0):
            minefieldArray[r][c] += 110   # Put Minesweeper to this cell and open this cell
        elif (minefieldArray[r][c] == -1):
            return False                  # Blow up!!!

    return True

"""
It is temporary function.
Print all Minefield to console
"""
def print_Minefield() -> bool:

    # Print all Minefield
    for r in range(1, MINEFIELD_ROWS + 1):
        for c in range(1, MINEFIELD_COLUMNS + 1):
            print(f"[{minefieldArray[r][c]}]",end='')
        print()

fill_Minefield(20)

print_Minefield()

print("Do step: ", end='')
r, c =  map(int, input().split())

while ((r != 0) or (c != 0) ):

    if (not do_Step_Minefield(r, c)):
        print("You are blowed up!!!")
        break
    print_Minefield()
    print("Do step: ", end='')
    r, c =  map(int, input().split())
