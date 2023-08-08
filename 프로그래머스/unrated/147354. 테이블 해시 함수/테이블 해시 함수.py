def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x : (x[col - 1], -x[0]))
    
    S_i = []
    for i in range(row_begin - 1, row_end):
        s = 0
        for j in data[i]:
             s += j %  (i + 1)
        S_i.append(s)
    tmp = None
    for each in S_i:
        
        
        if tmp == None:
            tmp = each
            continue
        
        tmp = tmp ^ each
        
    return tmp
    