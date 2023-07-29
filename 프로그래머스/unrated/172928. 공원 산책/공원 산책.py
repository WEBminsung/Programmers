def solution_(park,routes):
    a,b='e 2'.split(' ')
    print(a,b)
def solution(park, routes):
    
    answer = []
    row =0
    col =0
    for r, i in enumerate(park):
        for c,j in enumerate(i):
            if j == "S":
                row =r
                col =c
    row_len = len(park) - 1 
    col_len = len(park[0]) - 1
    
    for route in routes:
        direction, distance = route.split()
        distance = int(distance)
        if direction == 'N' :
            flag = True
            for i in range(1,distance + 1):
                if row - i >= 0 and park[row - i][col] != 'X':
                    continue
                else: 
                    flag = False
                    break
                
            if flag:
                row -= distance
                
        elif direction == 'S':
            flag = True
            for i in range(1,distance + 1):
                
                if row + i <= row_len and park[row + i][col] != 'X':
                    pass
                else:
                    flag = False
            if flag:
                row += distance
                
        elif direction == 'W':
            flag = True
            for i in range(1, distance + 1):
                if col - i >= 0 and park[row][col - i] != 'X':
                    pass
                else:
                    flag = False
                    break
            if flag:
                col -= distance
                
        elif direction == 'E':
            flag = True
            for i in range(1, distance + 1):
                if col + i <= col_len and park[row][col + i] != 'X':
                    pass
                else:
                    flag =False
                    break
            if flag:
                col += distance
                
            
        # print(row,col)
    
    

    return [row,col]