def solution(name):
    answer = 0
    lst = [chr(i) for i in range(ord('A'),ord('Z')+1)]
    half = (ord('A')+ord('Z'))//2
    
    for i in name:
        if ord(i)<=half:
            answer += ord(i)-ord('A')
        else:
            answer += ord('Z')-ord(i)+1
    m,t=0,0
    for i in range(len(name)):
        if name[i] == 'A':
            t += 1      
        else:
            print(t, i)
            m = min(i, (i-t)*2+len(name)-i-1)
            t=0
            
    if m == 0:
        answer+=len(name)-1
    else:
        answer+=m
    return answer
