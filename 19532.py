a,b,c,d,e,f=map(int,input().split())
if a==0:
    y=c/b
    x=(f-e*y)/d
else:
    y=(c*d-f*a)/(b*d-e*a)
    x=(c-b*y)/a
print(int(x),int(y))
