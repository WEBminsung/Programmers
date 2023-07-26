from collections import defaultdict #
def solution(picks, minerals):
    answer=0
    # 5개씩 나눠서 담기
    dic = []
    i = 0
    flag = False
    for _ in range(sum(picks)):
        
        try:
            tmp = minerals[i:i+5]
            i += 5
        except:
            tmp = minerals[i:i+len(minerals) % 5]
            flag = True
        value = (tmp.count('diamond') * 25) + (tmp.count('iron') * 5) + (tmp.count('stone') * 1)
        dic.append([value,tmp])
        if flag:
            break
    
    for i in sorted(dic,reverse=True):
        pick = None
        if picks[0] > 0:
            picks[0] -= 1
            pick = 3
        elif picks[1] > 0:
            picks[1] -= 1
            pick = 2
        elif picks[2] > 0:
            picks[2] -= 1
            pick = 1
            
        for mineral in i[1]:
            if pick == 3:
                answer += 1
            elif pick == 2:
                if mineral == 'diamond':answer += 5
                else: answer += 1
            else:
                if mineral == 'diamond':answer += 25
                elif mineral == 'iron':answer += 5
                else: answer += 1
    
    
    return answer