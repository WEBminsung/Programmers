def solution(li):
    count=0
    for i in range(1,len(li)+1):
        if i<=func(i,li):
            count+=1
    return count    
    

def func(n,li):
    count=0
    for i in li:
        if i>=n:
            count+=1
    return count