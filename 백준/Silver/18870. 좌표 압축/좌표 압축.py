n = int(input())
lst = list(map(int, input().split()))
lst_sort = sorted(list(set(lst)))
dic = {lst_sort[i] : i for i in range(len(lst_sort))}

for i in lst:
    print(dic[i], end = ' ')
