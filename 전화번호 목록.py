def solution(phone_book):
    answer = True
    ph = phone_book.copy()
    for i in phone_book:
        ph.remove(i)
        for k in ph:
            m = min(len(i), len(k))
            if i[:m] == k[:m]:
                answer = False
                break
    return answer
