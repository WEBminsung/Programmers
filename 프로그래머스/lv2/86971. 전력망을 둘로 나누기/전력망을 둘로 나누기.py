from collections import defaultdict
def solution(n, wires):
#     que = []
#     que.extend([1,2,3])
    
#     return
    answer = -1
    diff = []
    for k in range(len(wires)):
        sub_wires = wires.copy()
        wires_dict = defaultdict(list)    
        del sub_wires[k]
        
        # print(sub_wires)
        for i, j in sub_wires:

            wires_dict[i].append(j)
            wires_dict[j].append(i)

        
        # for key, value in wires_dict.items():
        #     print(key, value)
        
        
        cnt_list = set()

        for i in range(1, n + 1):


            que = [i]
            cnt = 0
            visit = set()

            while que:
                
                num = que.pop(0)
                if num in visit:continue    
                que.extend(wires_dict[num])
                visit.add(num)
                cnt += 1
                

            # print('num =' ,i)
            # print('cnt = ' ,cnt)
            
            cnt_list.add(cnt)
        # print(cnt_list)
        if len(cnt_list) == 1:
            return 0
        else:
            cnt_list = list(cnt_list)
            cnt_list.sort()
            diff.append(cnt_list[1] - cnt_list[0])
    
    return min(diff)