def solution(phone_book):
    dic = {}

    for x in phone_book:
        dic[x] = 0

    for x in phone_book:
        temp = ""
        for y in x:
            temp += y #몇 글자가 맞을지 모르니깐 하나씩 더 해봄
            if temp in dic and temp != x: #dic에 있으면서 자기 자신은 아닌 것
                return False

    return True
