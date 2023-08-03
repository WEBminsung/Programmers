def solution_(a,b,c):
    print(0/1)
def solution(today, terms, privacies):
    answer = []
    dic = {}
    y, m, d = map(int, today.split('.'))
    
    for term in terms:
        name, term = term.split(' ')
        term = int(term)
        
        new_y = y if m - term > 0  else y -1 - ((term - m) // 12)
        new_m = m - term if m - term  > 0 else 12 - ((term - m) % 12)
        new_d = d
        dic[name] = (new_y, new_m, new_d)
    for idx, i in enumerate(privacies):
        date, name = i.split(' ')
        y, m, d = map(int, date.split('.'))
        now_y, now_m, now_d = dic[name]
        
        date = y * 365 + m * 28 + d
        now_date = now_y * 365 + now_m * 28 + now_d
        if date <= now_date:
            answer.append(idx + 1)
            
        
        
        
    return answer