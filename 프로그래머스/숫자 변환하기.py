def solution(x, y, n):
    cnt, cntt = 0, 0
    y1 = y
    if x == y:
        cnt = 0
    while y1 > x:
        y1-=n
        cntt +=1
    if y1 != x:
        cntt = -1
    while y > x:
        if (y % 2 != 0) and (y % 3 != 0):
            y -= n
            cnt+=1
        elif y % 2 == 0:
            y /= 2
            cnt+=1
        else:
            y /= 3
            cnt+1

    if y != x:
        cnt = -1
    if cntt > 0 :
        cnt = min(cnt, cntt)
    return cnt
