#10871

N,X=map(int,input().split())
lst=list(map(int, input().split()))
for i in range(N):
    if lst[i]<X:
        print(lst[i],end=' ')

# sep: 구분자, end: 그 뒤 출력값 이어서 ex) end=' '라 했을 경우 커서가 엔터가 아닌 공백으로

# ("%s을 %d개 주세요."%("아이스크림", 10))
