n,m=map(int,input().split())
arr=list(map(int,input().split()))
def bf(n,m):
    result=0
    p1,p2,p3=0,1,2
    while p1!=(len(arr)-2): 
        total=(arr[p1]+arr[p2]+arr[p3])
        if total<=m:
            if total>=result:
                result=total
        p3+=1
        if p3==len(arr):
            p2+=1
            p3=p2+1
        if p2==len(arr)-1:
            p1+=1
            p2=p1+1
            p3=p1+2
    return result
print(bf(n,m))
# for 문 사용하는게 더 짧음
