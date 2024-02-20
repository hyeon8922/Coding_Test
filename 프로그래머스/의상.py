def solution(clothes):
    answer = 1
    lst, dic = [], {}
    for i in range(len(clothes)):
        lst.append(clothes[i][1])
    s = set(lst)
    for i in s:
        dic[i] = lst.count(i)
        
    for i in dic.values():
        answer *= (i+1)
            
    return answer-1
