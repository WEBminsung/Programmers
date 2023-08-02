import math
def solution_(a,b,c,d,e):
    x1, y1 = 1, 1
    x2, y2 = 2, 2
    a = (y2 - y1) / (x2 - x1)
    b = y1 - (a * x1)
    print ( a, b)
    x3, y3 = 3, 4
    print( 0 == (a * x3) + b - y3)
        
    
def solution(m, n, startX, startY, balls):
    answer = []
    x1 = startX
    y1 = startY
    for ball in balls:
        x2, y2 = ball
        dic = {}
        len_x, len_y = 0,0
        if not(x1 == x2 and y1 < y2):
            len_x = abs(x1 - x2)
            len_y = abs((n - y1) + (n - y2))
            dic['up'] =  (len_x ** 2) + (len_y ** 2)
        if not(x1 == x2 and y1 > y2):
            len_x = abs(x1 - x2)
            len_y = abs(y1 + y2)
            dic['down'] = (len_x ** 2) + (len_y ** 2)
        if not(y1 == y2 and x1 < x2):
            len_x = abs(m - x1 + m - x2)
            len_y = abs(y1 - y2)
            dic['right'] = (len_x ** 2) + (len_y **2)
        if not(y1 == y2 and x1 > x2):
            len_x = abs(x1 + x2)
            len_y = abs(y1 - y2)
            dic['left'] = (len_x ** 2) + (len_y ** 2)
        
        
        answer.append(min(dic.values()))
        print(dic)
        
    return answer
        
   
