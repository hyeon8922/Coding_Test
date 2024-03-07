def solution(answers):
    answer = []
    ans = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    score = [0 for i in range(3)]

    for i in range(len(answers)):
        for j in range(len(ans)):
            if answers[i] == ans[j][i % (len(ans[j]))]:
                score[j]+=1
    for i in range(len(score)):
        if score[i] == max(score):
            answer.append(i+1)
    return answer