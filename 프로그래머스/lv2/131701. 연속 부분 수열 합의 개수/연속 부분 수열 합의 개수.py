from collections import defaultdict
def solution(elements):
    answer = 0
    
    el_len = len(elements)
    count_dict = defaultdict(int)
    num_set = set()
    
    for i in range(el_len):
        for j in range(el_len):
            
            count_dict[j] += elements[(i + j) % el_len]
            

        # print(count_dict)
        num_set.update(count_dict.values())
        
    # print(num_set)
    return len(num_set)