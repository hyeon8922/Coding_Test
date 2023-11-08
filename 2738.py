n,m=map(int, input().split())
arr=[]
arr1=[]
arr2=[]
for i in range(n):
    row1=list(map(int,input().split()))
    arr1.append(row1)
for k in range(n):
    row2=list(map(int,input().split()))
    arr2.append(row2)
for i in range(n):
    for k in range(m):
        print(arr1[i][k]+arr2[i][k],end=' ')
    print()

# 그냥 넣고(append) 출력하면 되는 문제였음.
