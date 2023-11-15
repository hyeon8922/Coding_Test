#11021

x=int(input())
list=[]
n=1
while x>0:
    A,B=map(int, input().split())
    list.append(A+B)
    x-=1
for i in list:
    print('Case #{}: {}'.format(n,i))
    n+=1

# print() 안에 str+int 자료형 문제로 안됨.
