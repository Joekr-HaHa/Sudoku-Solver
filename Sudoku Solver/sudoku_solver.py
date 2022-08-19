import tkinter
import pygame
import random
#### BACKTRACKING ####
#1. Pick Empty Square
#2. Try all numbers
#3. As soon as find number that works, move to next
#4. Repeat
#5. Backtrack if no longer valid
#python resume projects

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]]

def solve(board):
    #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    #printBoard(board)
    #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    find=findEmpty(board)
    if not find:#this part is base case of recursion
        return True
    else:
        row, col=find
    for i in range(1,10):#1-9
        if valid(board,i,(row, col)):#if by adiign into board, is valid
            board[row][col]=i#then add it

            if solve(board):
                return True
            board[row][col]=0#reset value, set new value
    return False#will keep going through until true
    


def valid(board,num,pos):#pos ([0][1])
    #check row
    for i in range(len(board[0])):
        if board[pos[0]][i]==num and pos[1]!=i:#pos1 !=i means ignore where you juust put value
            return False

    #check column
    for i in range(len(board)):
        if board[i][pos[1]]==num and pos[0]!=i:
            return False
    #check 3x3 boxes
    box_x=pos[1]//3#pos[1] is the second value of tuple e.g (0,1) will be 1
    box_y=pos[0]//3#pos[0] is the first value of tuple e.g (0,1) will be 0
    #integer division ^
    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if board[i][j]==num and (i,j)!=pos:
                return False
    return True #if make it through these conditions then true


def printBoard(board):
    for i in range(len(board)):
        if i%3==0 and i !=0:
            print("------------------------")
        for j in range(len(board[0])):
            if j%3==0 and j!=0:
                print(" | ",end="")#end= means no \n

            if j==8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end='')

def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return(i,j) #row, column
    return None

printBoard(board)
solve(board)
print("#########################")
print("                         ")
print("#########################")
printBoard(board)
