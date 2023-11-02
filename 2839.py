n=int(input())
arr=[]
five=n//5
while five != -1:
    three=(n-five*5)//3
    if (n-five*5)%3==0:
        arr.append(five+three)
    five-=1
if len(arr)==0:
    print(-1)
else:
    print(min(arr))
