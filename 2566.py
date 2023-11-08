arr,arr_m=[],[]
for _ in range(9):
    row=list(map(int, input().split()))
    arr.append(row)
for k in range(9):
    arr_m.append(max(arr[k]))
print(max(arr_m))
print(arr_m.index(max(arr_m))+1,arr[arr_m.index(max(arr_m))].index(max(arr_m))+1)
