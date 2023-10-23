def solution(n, m, section):
    answer = 1
    t=1
    loca=section[0]
    while loca!=section[-1]:
        if loca+m-1>=section[t]:
            t+=1
            if t>=len(section):
                break
        else:
            loca=section[t]
            answer+=1
    return answer
