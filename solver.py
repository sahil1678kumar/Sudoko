from operator import le
from pickle import FALSE
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(bo) :
    find = find_empty(bo)
    if not find : 
        return True
    else :
        row,col = find
    
    for i in range(1,10) :
        if valid(bo,i,(row,col)) :
            bo[row][col] = i

            if solve(bo) : 
                return True
            
            bo[row][col] = 0;

    return False
     

def valid(bo, num, pos):
    # check rows
    for j in range(len(bo)) :
        if bo[pos[0]][j] == num and pos[1] != j :
            return False
    
    #check col
    for i in range(len(bo)) :
        if bo[i][pos[1]] == num and pos[0] != i :
            return False

    #check 3*3 squares
    box_i = pos[0] // 3
    box_j = pos[1] // 3

    for i in range(box_i*3, box_i*3 + 3) :
        for j in range(box_j*3, box_j*3 + 3) :
            if bo[i][j] == num and (i,j) != pos :
                return False

    return True

def print_board(bo):
    for i in range(len(bo)) : 
        if i%3 == 0 and i!= 0 :
            print("-----------------------")
        
        for j in range(len(bo)) :
            if j%3 ==0 and j!=0 :
                print(" | ", end = "")
            
            if j == 8 :
                print(bo[i][j])
            else :
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)) :
        for j in range(len(bo)) :
            if bo[i][j] == 0 :
                return (i,j) 

    return None