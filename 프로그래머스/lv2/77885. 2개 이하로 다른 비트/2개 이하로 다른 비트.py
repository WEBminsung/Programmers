def solution(numbers):
    answer = []
    # numbers = [15, 11]
    for num in numbers:
        binery = bin(num)[2:]
        # print('binery =', binery)
        e = 0
        for i in range(len(binery) - 1, -1 , -1):
            if binery[i] == '1':
                e += 1
            else:break
        # print(e)
        if e < 2:
            answer.append(num + 1)
            continue
        answer.append(num + 2 ** (e - 1))
    # print(answer)
    return answer