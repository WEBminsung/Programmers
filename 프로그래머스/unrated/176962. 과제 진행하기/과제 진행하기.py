
def solution(plans):
    answer = []
    tmp = []
    # 시작시간과 걸리는 시간 계산해서 넣기
    for name, start_time, time in plans:
        end_time = int(start_time[:2]) * 60 + int(start_time[3:]) + int(time)
        
        start_time = int(start_time[:2]) * 60 + int(start_time[3:])
        tmp.append([name, start_time,end_time])
    # plans를 바꾼 plans로 바꾸기
    plans = tmp
    # 시간을 기준으로 오름차순
    plans.sort(key = lambda x : x[1])
    stack = []
    for idx, plan in enumerate(plans):
        # 다음 과목 가져오기
        try:
            next_plan = plans[idx + 1]
        except:
            answer.append(plan[0])
            while stack:
                answer.append(stack.pop()[0])
        # 만약 현재 과제가 끝나는 시간보다 다음 과제 시작시간이 1분이라도 빠르다면?
        if plan[2] > next_plan[1]:
            stack.append([plan[0],plan[2] - next_plan[1]])
        # 현재 과제가 끝난후에 다음과제진행이 가능한경우
        else:
            # 다음과제가 시작하기까지의 텀동안 
            answer.append(plan[0])
            term = next_plan[1] - plan[2]
            while  stack:
                last_plan = stack.pop()
                if last_plan[1] <= term:
                    term -= last_plan[1]
                    answer.append(last_plan[0])
                else:
                    last_plan[1] -= term 
                    stack.append(last_plan)
                    break
                    
        
    
    
    return answer