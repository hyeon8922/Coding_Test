#2675

t=int(input())
new_s=[]
for i in range(t):
    r,s=map(str,input().split())
    for k in range(len(s)):
        new_s+=s[k]*int(r)
    print(*new_s,sep="")
    new_s=[]
# 리스트 하나씩 뺄 때 반복문 말고 포인터로 가능
