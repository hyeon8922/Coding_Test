def solution(progresses, speeds):
    answer = []
    
    # progresses가 남아있는 이상 계속 while
    while progresses:
        cnt=0
        
        # progresses가 없는데 pop 할 수 없으므로 progresses가 True인지 확인 추가
        while progresses and progresses[0] >=100:
            cnt+=1
            progresses.pop(0)
            speeds.pop(0)
        progresses = [(progresses[i] + speeds[i]) for i in range(len(progresses))]
        
        # cnt는 계속 넣어주는데 0이 아니면 넣어주지 않음
        if cnt != 0:
            answer.append(cnt)
    return answer 


# progresses에 speeds를 게속 더하면서 100이 넘을 시 cnt를 세고 pop으로 빼줌
