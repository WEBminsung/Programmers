from math import sqrt
def solution(r1, r2):
    r1_cnt = func(r1 ,True) - 4
    r2_cnt = func(r2) 
    
    
        
    answer = r2_cnt - r1_cnt
    return answer

def func(r , r1 = False):
    re = 0
    for x in range(1,r):
        y = sqrt((r**2) - (x**2))
        if y % 1 == 0:
            if r1:
                re += y - 1
            else:
                re += y
        else:
            re += (y // 1)
    re = re * 4
    re += r * 4
    
    return re