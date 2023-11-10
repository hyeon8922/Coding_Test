#1316

c=input()
lst=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in lst:
    c=c.replace(i,'*')
print(len(c))

# 별로 바꿔서 두 글자를 한 글자로 바꿔 센다.
