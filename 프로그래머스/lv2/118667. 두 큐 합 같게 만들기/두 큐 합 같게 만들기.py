def solution(queue1, queue2):
    
    answer = -2
    que1_sum = sum(queue1)
    que2_sum = sum(queue2)
    length = len(queue1) + len(queue2)
    
    def reverser(li):
        re = []
        for i in range(len(li) - 1, -1, -1):
            re.append(li[i])
        return re
    que1_sort = reverser(queue1 + queue2)
    que2_sort = reverser(queue2 + queue1)
    
    # print(que1_sort, que2_sort)
    
    cnt = 0
    # while cnt <= length * 2:
    while que1_sort and que2_sort:
        # print('que1_sort = ',que1_sort)
        # print('que2_sort = ',que2_sort)
        # print(que1_sum,'\n', que2_sum)
        # print()
        try:
            if que1_sum == que2_sum:
                return cnt
            cnt += 1
            if que1_sum > que2_sum:
                tmp = que1_sort.pop()
                que1_sum -= tmp
                que2_sum += tmp
            elif que1_sum < que2_sum:
                tmp = que2_sort.pop()
                que2_sum -= tmp
                que1_sum += tmp
            
        except Exception as e:
            print(e)
            break
    
    
    
    return  -1