def solution(numbers, target):
    answer = 0
    
    q = [[numbers[0], 0], [-1*numbers[0], 0]]
    
    while q:
        temp, now = q.pop()
        now += 1
        
        if now < len(numbers):
            q.append([temp + numbers[now], now])
            q.append([temp - numbers[now], now])
            
        else:
            if temp == target:
                answer += 1
    return answer