    

#3052

lst=[]
for k in range(10):
    n=int(input())
    lst.append(n%42)
lst=set(lst)
lst=list(lst)
print(len(lst))

# if _ not in list: 로도 가능.

# set:집합 사용시 중복 삭제됨.
