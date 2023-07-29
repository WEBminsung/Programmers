def solution(players, callings):
    answer = []
    name_dic = {} 
    rank_dic = {}
    for idx,name in enumerate(players):
        name_dic[name] = idx
        
    for name in callings:
        idx = name_dic[name] 
        front_name = players[idx - 1]
        name_dic[front_name] = idx
        name_dic[name] = idx - 1
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
        
    # print(players)
    # for i,j in sorted(name_dic.items(),key = lambda x:x[1]):
    #     answer.append(i)
    # sorted(name_dic.items(),)
    # print(name_dic.)
    
        
    
    return players