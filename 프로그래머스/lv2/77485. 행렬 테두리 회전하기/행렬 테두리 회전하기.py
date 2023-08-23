def solution(rows, columns, queries):
    answer = []
    # queries, rows, columns = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]	,6	,6	
    place = []
    for i in range(rows):
        place.append([0] + [j for j in range(i * columns + 1, (i + 1) * columns + 1)])
    place = [0] + place
    def show():
        for i in place:
            print(i)
            
    
    for que in queries:
        l = que[1]
        r = que[3]
        u = que[0]
        d = que[2]
        
        row, col = u, l
        col -= 1
        prev = None
        num_set = set()
    
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            row += dy
            col += dx

            while True:
                num_set.add(place[row][col])
                if prev == None:
                    prev = place[row][col]
                    row += dy
                    col += dx

                    continue
                tmp = place[row][col]
                place[row][col] = prev
                prev = tmp
                if l <= col + dx <= r and u <= row + dy <= d:
                    row += dy
                    col += dx
                else:
                    break
                    
        
        # show()
        answer.append(min(list(num_set)))
    return answer
        