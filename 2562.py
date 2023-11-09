#2562

lst=[]
for i in range(9):
    x=int(input())
    lst.append(x)
max=lst[0]
for k in range(9):
    if lst[k]>=max:
        max=lst[k]
        num=k+1
print(max,num,sep='\n')
