def solution(name, yearning, photo):
    answer = [0 for i in range(len(photo))]
    for i in range(len(photo)):
        for j in name:
            answer[i]+=(photo[i].count(j)*yearning[name.index(j)])
    return answer
