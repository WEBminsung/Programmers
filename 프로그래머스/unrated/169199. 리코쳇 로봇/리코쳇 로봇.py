from collections import deque

a=["...D...",
   "..DG...",
   ".......",
   "D......",
   "..D...."]
def solution_(board):
    if '':
        print('a')
def solution(board):
    
    row = 0
    col = 0
    row_max = len(board) - 1 
    col_max = len(board[0]) - 1
    for i, board_row in enumerate(board):
        
        if 'G' in board_row:
            row = i
            col = board_row.index('G')
            break
    
    dic = {}
    dic['up'] = row - 1 < 0 or board[row - 1][col] == 'D'
    dic['down'] = row + 1 > row_max or board[row + 1][col] == 'D'
    dic['left'] = col - 1 < 0 or board[row][col - 1] == 'D'
    dic['right'] = col + 1 > col_max or board[row][col + 1] == 'D'
    
    go = None
    sub_go = False
    if  not dic['down'] and dic['up']:
        go = 'down'
        if not dic['left'] and dic['right']:
            sub_go = True
        elif not dic['right'] and dic['left']:
            sub_go = True
            
    elif not dic['up'] and dic['down']:
        go = 'up'
        if not dic['left'] and dic['right']:
            sub_go = True
        elif not dic['right'] and dic['left']:
            sub_go = True
    elif not dic['left'] and dic['right']:
        go = 'left'
        if not dic['up'] and dic['down']:
            sub_go = True
        elif not dic['down'] and dic['up']:
            sub_go = True
    elif not dic['right'] and dic['left']:
        go = 'right'
        if not dic['up'] and dic['down']:
            sub_go = True
        elif not dic['down'] and dic['up']:
            sub_go = True
    else:return -1
    
    
    
    
    visit = []
    que = deque()
    que.append(([row,col],go))
    
    count = 1
    if sub_go:
        count = 2
    
    stack_count = 0
    move = 1
    
    while que:
        
        
        
        rowcol, go = que.popleft()
        
        if rowcol in visit :
            
            
            if count - 1 == 0:
                count = stack_count
                move += 1
                stack_count = 0
            else:
                count -= 1
            
            continue
            
        if not sub_go:
            visit.append(rowcol)
        row = rowcol[0]
        col = rowcol[1]
        
        
        cnt = 0
        while True:
            if board[row][col] == 'R':
                
                return move
            
            left = col - 1 < 0 or board[row][col - 1] == 'D'
            right = col + 1 > col_max or board[row][col + 1] == 'D'
            up = row - 1 < 0 or board[row - 1][col] == 'D'
            down = row + 1 > row_max or board[row + 1][col] == 'D'
            
            if (go == 'up' or go == 'down') and not(left and right) and (left or right):
                if left:
                    que.append(([row,col],'right'))
                    cnt += 1
                    
                elif right:
                    que.append(([row,col],'left'))
                    cnt += 1
                    
                    
                
                    
            if (go == 'left' or go == 'right') and not(up and down) and (up or down):
                if up:
                    que.append(([row,col],'down'))
                    cnt += 1
                    
                elif down:
                    que.append(([row,col],'up'))
                    cnt += 1
                    
                
            if go == 'up' and up:
                break
            elif go == 'up' and not up:
                row -= 1
            if go == 'down' and down:
                break
            elif go == 'down' and not down:
                row += 1
            if go == 'left' and left:
                break
            elif go == 'left' and not left:
                col -= 1
            if go == 'right' and right:
                break
            elif go == 'right' and not right:
                col += 1
        stack_count += cnt    
        if sub_go:
            stack_count -= 1
            sub_go = False
        
        
        
        
        if count - 1 == 0:
            count = stack_count
            move += 1
            
            stack_count = 0
        else:
            count -= 1
        
        
    return -1