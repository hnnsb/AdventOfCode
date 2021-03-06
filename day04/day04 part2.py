import numpy as np
    
def main():
    numbers = getInput1('day04/input day04_1.txt')
    boards = getInput('day04/input day04_2.txt')
    #print(numbers)
    #print(boards)
    
    boardsCopy = boards[:]
    winningBoard = []
    winningNumber = 0
    winningList = [0]*len(boards)
    for n in numbers:

        for b_index, board in enumerate(boards):
            
            boardC = board.copy()
            for row_index, row in enumerate(board):
                
                for num_index, num in enumerate(row):
                    
                    if board[row_index][num_index] == n:
                        boardC[row_index][num_index] = -1
           

            if(testForWin(boardC)):
                winningList[b_index] = 1
                if(sum1(winningList) == len(boards)):
                    winningBoard = boardC.copy()
                    winningNumber = n
                    break
        
        if(winningBoard != []):
            break
    
    print(len(boards))
    print(winningList)
    print(winningBoard)
    print(winningNumber)

    sum = 0
    for row in winningBoard:
        for num in row:
            if num != -1:
                sum += num
    
    print(sum * winningNumber)


def sum1(list):
    sum = 0
    for i in list:
        sum += i

    return sum

def testForWin(board):
    for row in board:
        sum = 0
        for num in row:
            sum += num
            
            if(sum == -5):
                return True

    for i in range(len(board)):
        sum = 0
        for j in range(len(board[0])):
            sum += board[j][i]
        
        if(sum== -5):
            return True

    return False


def getInput1(path):
    file = open(f'{path}','r')
    inp = file.read().split(',')
    
    inp = [int(x) for x in inp ]
    
    file.close()

    return inp


def getInput(path):
    file = open(f'{path}','r')
    inp = [[int(n) for n in line.split()] for line in file]
    data = []
    board = []
    for row in inp:
        if(row == []):
            data.append(board)
            board = []
            continue
        
        board.append(row)
        
    
    file.close()

    
    
    return data
   

if __name__ == '__main__':
    main()