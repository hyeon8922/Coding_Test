#2480

a,b,c=map(int, input().split())
if a==b==c:
    print(10000+(a*1000))
elif a!=b!=c and a!=c:
    print(max(a,b,c)*100)
else:
    if a==b or a==c:
        print(1000+(a*100))
    else:
        print(1000+(b*100))

# a!=b!=c는 a!=c까지 보장해주지 않는다. (순서대로 판단)

# max(a,b,c)


