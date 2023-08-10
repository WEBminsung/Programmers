def solution(citations):
    citations.sort()
    size = len(citations)
    for i in range(size + 2):
        while citations:
            if i > citations[0]:
                citations.pop(0)
                continue
            break
        if i > len(citations):
            break
        # print(citations)
    # print(i - 1)
    
    return i -1
    