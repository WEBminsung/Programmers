def solution(n, left, right):
    answer = []
    
    start_row = (left // n) + 1
    end_row = (right // n) + 1
    
    # print(start_row)
    # print(end_row)
    li = []
    for i in range(start_row, end_row + 1):
        for j in range(1, n + 1):
            if j < i:
                li.append(i)
            else:
                li.append(j)
    
    left_col = left % n
    right_col = n - ((right % n) + 1)
    
    length = len(li)
    # print(left_col, right_col)
    # print(li)
    return li[left_col : length - right_col]
    
    