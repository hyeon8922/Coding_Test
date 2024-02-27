def solution(data, ext, val_ext, sort_by):
    answer = []
    lst = ['code', 'date', 'maximum', 'remain']
    t = lst.index(ext)
    for i in range(len(data)):
        if data[i][t] < val_ext:
            answer.append(data[i])
    answer.sort(key=lambda x : x[lst.index(sort_by)])
    return answer