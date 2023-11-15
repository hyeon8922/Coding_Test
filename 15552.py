#15552

import sys
x=int(sys.stdin.readline())
list=[]
while x>0:
    A,B=map(int,sys.stdin.readline().split())
    list.append(A+B)
    x-=1
for i in list:
    print(i)

# import sys

# sys.stdin.readline > 시간초과 줄이기

# .rstrip() > 문자열 저장일 경우 개행 없애기 
