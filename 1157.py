#1157

s=input().upper()
set_s=set(s)
max=0
for i in set_s:
    if s.count(i)>max:
        max=s.count(i)
        alpha=i
    elif s.count(i)==max:
        if alpha != i:
            alpha='?'
print(alpha)

# 반복을 없애고 시간을 줄이기 위해 set으로 중복을 없애준다.
