def solution(word):
    answer = 0
    dic = {'A' : 1, 'E' : 2, 'I' : 3, 'O' : 4, 'U' : 5, 'x' : 0}
    tmp = []
    for each in word.ljust(5, 'x'):
        tmp .append( dic[each])
    # print(tmp)
    word = tmp
    prev = 0
    for each in word[::-1]:
        if each == 1:
            answer += 1
        elif each > 1:
            val = ((prev * 5) + 1) * (each - 1) + 1
            # print(val)
            answer += val
        prev = (prev * 5) + 1
        # print(prev)
    return answer
    
    
    