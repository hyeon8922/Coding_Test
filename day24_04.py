num = int(input())
cnt = 0

while num != 1:
    if num % 5 == 0:
        num = num//5*4
        cnt+=1
    elif num % 3 == 0:
        num = num//3*2
        cnt+=1
    elif num % 2 == 0:
        num = num//2
        cnt+=1
    else: 
        num = 1
        cnt = -1

print(cnt)
