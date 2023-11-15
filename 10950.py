#10950

x=int(input())
list=[]
while x>0:
    a,b=map(int, input().split())
    list.append(a+b)
    x-=1
for i in list:
    print(i)
