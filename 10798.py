#10798

arr=[]
le=[]
for _ in range(5):
    row=list(input())
    arr.append(row)
    le.append(len(row))
for i in range(max(le)):
    for k in range(5):
        if i<le[k]:
            print(arr[k][i],end='')
# le 가로 길이 array를 만들어서 넘어가지 않도록 if문으로 제한을 걸어준다.         
