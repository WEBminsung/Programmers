def solution(cap, n, deliveries, pickups):
    answer = -1
    deliveries_idx = len(deliveries)
    pickups_idx = len(pickups)
    sum_distance = 0
    while deliveries or pickups:
        deliveries_n = cap
        pickups_n = cap
        distance = 0
        while deliveries:

            el = deliveries.pop()
            if el == 0:
                deliveries_idx -= 1
                continue
            else:
                if deliveries_n < el:
                    deliveries.append(el - deliveries_n)
                    if distance < deliveries_idx:distance = deliveries_idx

                    break
                else:
                    deliveries_n -= el
                    if distance < deliveries_idx:distance = deliveries_idx
                    deliveries_idx -= 1
                    
        while pickups:
            el = pickups.pop()
            if el == 0:
                pickups_idx -= 1
                continue
            else:
                if pickups_n < el:
                    pickups.append(el - pickups_n)
                    if distance < pickups_idx:distance = pickups_idx

                    break
                else:
                    pickups_n -= el
                    if distance < pickups_idx:distance = pickups_idx
                    pickups_idx -= 1
        sum_distance += distance * 2
            
    
    return sum_distance
