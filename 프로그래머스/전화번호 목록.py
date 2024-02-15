def solution(phone_book):
    answer = True
    dic={}
    for p in phone_book:
        dic[p] = 0
    for i in phone_book:
        temp = ''
        for j in i:
            temp += j
            if temp in dic and temp != i:
                answer = False
    return answer
