def solution(places):
    answer = []
    # places = [["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]]
    for place in places:
        row_len = len(place)
        col_len = len(place[0])
        flag = False
        for row in range(len(place)):
            
            for col in range(len(place[0])):
                if place[row][col] == 'P':
                    if row + 1 < row_len:
                        if place[row + 1][col] == 'P':
                            answer.append(0)
                            # print(row + 1, col)
                            flag = True
                            break
                        if ((row + 2 < row_len) and place[row + 2][col] == 'P') and place[row + 1][col] == 'O':
                            answer.append(0)
                            # print(row + 2, col)
                            flag = True
                            break
                    if row - 1 >= 0:
                        if place[row - 1][col] == 'P':
                            answer.append(0)
                            # print(row - 1, col)
                            flag = True
                            break
                        if ((row - 2 >= 0) and place[row - 2][col] == 'P') and place[row - 1][col] == 'O':
                            answer.append(0)
                            # print(row - 2, col)
                            flag = True
                            break
                    if col + 1 < col_len:
                        if place[row][col + 1] == 'P':
                            answer.append(0)
                            # print(row, col + 1)
                            flag = True
                            break
                        if ((col + 2 < col_len) and place[row][col + 2] == 'P') and place[row][col + 1] == 'O':
                            answer.append(0)
                            # print(row, col + 2)
                            flag = True
                            break
                    if col - 1 >= 0:
                        if place[row][col - 1] == 'P':
                            answer.append(0)
                            # print(row, col - 1)
                            flag = True
                            break
                        if ((col - 2 >= 0) and place[row][col - 2] == 'P') and place[row][col - 1] == 'O':
                            answer.append(0)
                            # print(row, col - 2)
                            flag = True
                            break
                    if row + 1 < row_len and col + 1 < col_len:
                        if (place[row + 1][col] != 'X' or place[row][col + 1] != 'X') and place[row + 1][col + 1] == 'P':
                            answer.append(0)
                            # print(row + 1, col + 1)
                            flag = True
                            break
                    if row + 1 < row_len and col - 1 >= 0:
                        if (place[row + 1][col] != 'X' or place[row][col - 1] != 'X') and place[row + 1][col - 1] == 'P':
                            answer.append(0)
                            # print(row + 1, col - 1)
                            flag = True
                            break
                    if row - 1 >= 0 and col + 1 < col_len:
                        if (place[row - 1][col] != 'X' or place[row][col + 1] != 'X') and place[row - 1][col + 1] == 'P':
                            answer.append(0)
                            # print(row - 1, col + 1)
                            flag = True
                            break
                    if row - 1 >= 0 and col - 1 >= 0:
                        if (place[row - 1][col] != 'X' or place[row][col - 1] != 'X') and place[row - 1][col - 1] == 'P':
                            answer.append(0)
                            # print(row - 1, col - 1)
                            flag = True
                            break
                    
            if flag:
                break
        if not(flag):
            answer.append(1)
    print(answer)
    return answer
