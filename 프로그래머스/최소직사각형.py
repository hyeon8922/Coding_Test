def solution(sizes):
    lst = []
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    for i in range(len(sizes)):
        lst.append(sizes[i][1])
    ans = max(sizes)[0] * max(lst)
    return ans
