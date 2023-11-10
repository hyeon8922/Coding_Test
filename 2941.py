#2941

c=input()
cnt=0
lst=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in lst:
    cnt+=c.count(i)
    c=c.replace(i,'')
print(cnt+len(c))
