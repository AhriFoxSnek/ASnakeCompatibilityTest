# originally written by discord user: yelr
# mostly optimized

import numpy
import math 
 
boardState = [0] * 9
minimaxSeed = 4

def printBoard(board) :
    boardDisp = [' '] * 9
    i = 0
    while i < len(board):
        if board[i] == 1 :
            boardDisp[i] = 'X'
        elif board[i] == -1 :
         boardDisp[i] = 'O'
        else :
            boardDisp[i] = ' '
        i += 1
    print('-----')
    print(boardDisp[0], boardDisp[1], boardDisp[2])
    print(boardDisp[3], boardDisp[4], boardDisp[5])
    print(boardDisp[6], boardDisp[7], boardDisp[8])
    print('-----')

def rowColumn(row, column) :
    i = (3 * row) + column
    return i

def playerInput(player) :
    row = int(input('Row? '))
    column = int(input('Column? '))
    if boardState[rowColumn(row, column)] == 0 :
        boardState[rowColumn(row, column)] = player
        printBoard(boardState)
    else: 
        if checkWin(boardState) == 0 :
            printBoard(boardState)
            print('Square already filled. Try again')
            playerInput(player)
        else :
            return

def checkWin(board) :
    winIndices =  [[0,3,6], [1,4,7], [2,5,8], [0,1,2], [3,4,5], [6,7,8], [0,4,8], [2,4,6]]
    for element in winIndices :
        winCheckSum = (board[element[0]] + board[element[1]] + board[element[2]]) / 3
        if abs(winCheckSum) == 1 :
            return winCheckSum
    if 0 in board :
        return 2
    else :
        return 0
    
def moveSearch(board, player, depth) :
    winState = checkWin(boardState)
    if abs(winState) == 1 :
        if depth == 0 :
            return
        else :
            return winState * player * -1
    elif winState == 0: 
        if depth == 0 :
            return
        else :
            return 0
    elif winState == 2 :
        moveList = []
        i = 0
        while i < 9 :
            if board[i] == 0 :
                moveList.append(i)
            i += 1
        j = 0
        valueList = [0] * len(moveList)
        while j < len(moveList) :
            board[moveList[j]] = player
            valueList[j] = moveSearch(board, -1 * player, depth + 1)
            board[moveList[j]] = 0
            j += 1
        if depth == 0 :
            maxValue = max(valueList)
            maxIndices = numpy.flatnonzero(numpy.array(valueList) == maxValue)
            boardStateInt = sum([(2**j)*abs(boardState[j]) + 1 + minimaxSeed for j in range(len(valueList))])
            boardStateSeed = int(((100*abs(math.cos(boardStateInt)))%1)*100) % len(maxIndices)
            return moveList[maxIndices[boardStateSeed]]
        else :
            return max(valueList) * -1

def minimaxMove(board, player) :
    board[moveSearch(board, player, 0)] = player

def minimaxGame() :
    i = 0
    while checkWin(boardState) == 2 :
        minimaxMove(boardState, (-1)**i)
        printBoard(boardState)
        i += 1

minimaxGame()