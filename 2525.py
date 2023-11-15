#2525

H,M=map(int,input().split())
x=int(input())
y=(M+x)//60
if H+y>=24 and (M+x)>=60:
    print(H+y-24,(M+x)%60)
elif (M+x)>=60:
    print(H+y,(M+x)%60)
else:
    print(H,M+x)
