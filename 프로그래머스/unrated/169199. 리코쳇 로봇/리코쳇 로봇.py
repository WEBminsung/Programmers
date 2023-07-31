import heapq
def solution(board):
    start = 0
    for row,i in enumerate(board):
        for col,j in enumerate(i):
            if j == 'R':
                start = (row, col)   
    len_row = len(board)
    len_col = len(board[0])
    row_max = len_row - 1
    col_max = len_col - 1
    def dickstra(start):
        
        distances = [[float('inf')] * len_col for i in range(len_row)]
        distances[start[0]][start[1]] = 0
        q = []
        heapq.heappush(q, [0,start])
        k = 0
        while q:
        # while k < 4:
            k += 1
            current_distance, current_destination = heapq.heappop(q)
            row = current_destination[0]
            col = current_destination[1]
            
            dic = {'up':False, 'down':False, 'left':False, 'right':False}
            i = 0
            while not(dic['up'] and dic['down'] and dic['left'] and dic['right']):
                i += 1
                
            
                
                if (row - i < 0 or board[row - i][col] == 'D') and not dic['up']:
                    dic['up'] = (row - i + 1,col)
                    if board[row - i + 1][col] == 'G':
                        return current_distance + 1
                        
                    
                if (row + i > row_max or board[row + i][col] == 'D') and not dic['down']    :
                    dic['down'] = (row + i - 1,col)
                    if board[row + i - 1][col] == 'G':
                        return current_distance + 1
                    
                if (col - i < 0 or board[row][col - i] == 'D') and not dic['left']:
                    dic['left'] = (row,col - i + 1)
                    if board[row][col - i + 1] == 'G':
                        return current_distance + 1
                if (col + i > col_max or board[row][col + i] == 'D') and not dic['right']:
                    dic['right'] = (row,col + i - 1)
                    if board[row][col + i - 1] == 'G':
                        return current_distance + 1
                    
            
            for new_destination in dic.values():
                
                row, col = new_destination
                distance = current_distance + 1
                
                if distances[row][col] > distance:
                    distances[row][col] = distance
            
                    heapq.heappush(q, [distance, (row,col)])
            
        return -1
            
        
    
    
    return(dickstra(start))
    
        
    
    