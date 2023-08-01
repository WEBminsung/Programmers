from collections import defaultdict
import heapq
def solution(n, roads, sources, destination):
    answer = []
    graph = defaultdict(list)
    for i in roads:
        s = i[0]
        e = i[1]
        graph[s].append(e)
        graph[e].append(s)
    
    distances = {node : float('inf') for node in graph.keys()}
    distances[destination] = 0
    q = []
    heapq.heappush(q,(0,destination))
    while q:
        
        current_distance, current_destination = heapq.heappop(q)
        if current_distance < distances[current_destination]:
            continue
        for new_destination in graph[current_destination]:
            distance = current_distance + 1
            if distances[new_destination] > distance:
                distances[new_destination] = distance
                heapq.heappush(q, (distance, new_destination))
    s = set(distances.keys())
    
    for i in sources:
        if i in s and not distances[i] == float('inf') :
            answer.append(distances[i])
        else:
            answer.append(-1)
    return answer