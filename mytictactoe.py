# My first every project, SO excited!
"""
ALGORITHM:
Tic Tac Toe board
#It is like an array that contains other arrays
[ 
    [-, -, -],
    [-, -, -],
    [-, -, -]
]
user-input --> registers as one of the slots on the board 
They can enter numbers 1-9 (9 spaces- 1,2,3- first line and so on)
Anything else apart from 1-9: invalid entry
1. Check if number is picked form 1-9
2. Check if user-input is already taken (since it cannot be repeated)
3. Add it to the board
4. Check if user won: check rows, columns and diagonals
5. Toggle between users after each successful move
"""
# 1. Create the board- 2D array with 3 arrays
board =
[ 
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]