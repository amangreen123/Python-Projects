symbol = [ " ", "x", "o" ]

def printRow(row):
# initialize output to the left border
    output = "|"
# for each square in the row...
    for i in range (3):
# add to output the symbol for this square followed by a border
        output = output + " " + symbol[row[i]] + "|"
# print the completed output for this row
    print(output)

def printBoard(board):
# print the top border
    print("+--------+")
# for each row in the board...
    for i in range (3):
# print the row
        printRow(board[i])
# print the next border
        print("+--------+")

def markBoard(board, row, col, player):   
        # check to see whether the desired square is blank
        if board[row][col] == 0:
        #if so, set it to the player number
            board[row][col] = player
        else:
            print("Please pick another one")
            
    
def getPlayerMove():
    row = int(input("Enter a row for the player (1-3)"))
    col = int(input("Enter a column for the player(1-3)"))
    return (row - 1, col -1)

def hasBlanks(board):
    output = "|"
# for each row in the board...
    for i in range(0,3):
# for each col in the row...
        for j in range(0,3):
      # output = output + " " + symbol[row[i]] + "|"
            # check whether the square is blank
            if board[i][j] == 0:
                # if so, return True
                return True
# if no square is blank, return False
    return False
def main():
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]] # TODO replace this with a three-by-three matrix of zeros
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 + 1 # switch player for next turn
    # JA: You need to call printBoard again at the end
    printBoard(board)

main()
