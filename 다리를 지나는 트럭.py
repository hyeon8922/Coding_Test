def solution(bridge_length, weight, truck_weights):
    answer = 1
    arrive = truck_weights.copy()
    
    while len(arrive)!=0:
        ing = []
        truck_weights = arrive.copy()
        for i in truck_weights:
            if sum(ing)+i <= weight:
                ing.append(i)
                arrive.remove(i)
            else:
                print(ing, answer)
                break
        answer+=(bridge_length+len(ing)-1)
    return answer
